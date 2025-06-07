# utils/wire_set_cert_refresher.py
"""
Utility module for refreshing wire set certificate data from SharePoint.

Refactored to use WireSetCertSchema for validation and type safety.
"""

import io
import logging
from datetime import datetime
from typing import Any, Dict, List, Optional

import pandas as pd
from marshmallow import ValidationError
from sqlalchemy.orm import Session

from db.models import WireSetCert
from utils.database import SessionLocal
from utils.schemas import WireSetCertResult, WireSetCertSchema
from utils.sharepoint_client import SharePointClient


class WireSetCertRefresher:
    """Handles refreshing wire set certificate data from SharePoint."""

    def __init__(self, session: Optional[Session] = None):
        """
        Initialize the refresher.

        Args:
            session: Optional database session. If None, creates a new one.
        """
        self.session = session or SessionLocal()
        self.logger = logging.getLogger(__name__)
        self.schema = WireSetCertSchema()

        self.sharepoint_site = None  # Will be set from config
        self.pyro_folder_path = "Shared Documents/Pyro"
        self.wiresetcerts_filename = "WireSetCerts.xlsx"
        # Excel column mapping - based on actual Excel file structure
        # Excel headers are in this exact order:
        # ["asset_id", "serial_number", "asset_tag", "custom_order_number",
        #  "service_date", "next_service_date", "certificate_number",
        #  "wire_roll_cert_number", "type"]
        self.excel_headers = [
            "asset_id",
            "serial_number",
            "asset_tag",
            "custom_order_number",
            "service_date",
            "next_service_date",
            "certificate_number",
            "wire_roll_cert_number",
            "type",  # This maps to wire_set_group in our database
        ]

        # Mapping from Excel header to database field
        self.header_to_field_mapping = {
            "asset_id": "asset_id",
            "serial_number": "serial_number",
            "asset_tag": "asset_tag",
            "custom_order_number": "custom_order_number",
            "service_date": "service_date",
            "next_service_date": "next_service_date",
            "certificate_number": "certificate_number",
            "wire_roll_cert_number": "wire_roll_cert_number",
            "type": "wire_set_group",  # Excel "type" column -> database "wire_set_group"
        }

    def refresh_wire_set_certs(self) -> WireSetCertResult:
        """
        Refresh wire set certificate data from SharePoint.

        Returns:
            Dict containing refresh operation results
        """
        result = WireSetCertResult(
            status="success",
            message="",
            records_processed=0,
            records_added=0,
            records_updated=0,
            errors=[],
        )

        try:
            # Download the Excel file from SharePoint
            excel_data = self._download_wiresetcerts_file()

            if not excel_data:
                result.status = "error"
                result.message = "Failed to download WireSetCerts.xlsx"
                return result

            # Parse the Excel file with validation
            wire_set_mappings = self._parse_wiresetcerts_excel(excel_data)

            if not wire_set_mappings:
                result.status = "warning"
                result.message = "No wire set mappings found in file"
                return result

            # Update the database
            update_result = self._update_wire_set_certs_table(wire_set_mappings)
            result.update(update_result)

            self.logger.info(f"Wire set cert refresh completed: {result}")

        except Exception as e:
            self.logger.error(f"Error during wire set cert refresh: {e}")
            result.status = "error"
            result.message = f"Refresh failed: {str(e)}"
            result.errors.append(str(e))

        return result

    def _download_wiresetcerts_file(self) -> Optional[bytes]:
        """
        Download the WireSetCerts.xlsx file from SharePoint.

        Returns:
            File content as bytes, or None if download failed
        """
        try:
            # Use the existing SharePoint client to get file content
            sharepoint_client = SharePointClient()

            # Get the file reference first
            file_ref = sharepoint_client.get_wiresetcerts_file()

            if not file_ref.get("id"):
                self.logger.error("WireSetCerts.xlsx file not found in SharePoint")
                return None

            # Download the file content as bytes
            file_content = sharepoint_client.download_file_content(
                file_ref["id"], sharepoint_client.drive_id
            )

            self.logger.info(
                f"Successfully downloaded WireSetCerts.xlsx ({len(file_content)} bytes)"
            )
            return file_content

        except Exception as e:
            self.logger.error(f"Error downloading WireSetCerts.xlsx: {e}")
            return None

    def _parse_wiresetcerts_excel(self, excel_data: bytes) -> List[Dict[str, Any]]:
        """
        Parse the WireSetCerts.xlsx file using pandas for robust data handling.

        Args:
            excel_data: Raw Excel file content

        Returns:
            List of validated wire set certificate dictionaries
        """
        try:
            # Use pandas to read the Excel file from bytes
            df = pd.read_excel(io.BytesIO(excel_data), engine="openpyxl")

            self.logger.info(
                f"Successfully loaded Excel file with {len(df)} rows and columns: {df.columns.tolist()}"
            )

            # Clean column names (normalize to lowercase and strip whitespace)
            df.columns = df.columns.str.strip().str.lower()

            # Create column mapping from Excel headers to database field names
            column_mapping = {}
            for excel_header, db_field in self.header_to_field_mapping.items():
                excel_header_norm = excel_header.strip().lower()
                if excel_header_norm in df.columns:
                    column_mapping[excel_header_norm] = db_field
                    self.logger.debug(f"Mapped '{excel_header_norm}' -> '{db_field}'")
                else:
                    self.logger.warning(
                        f"Expected column '{excel_header}' not found in Excel file"
                    )

            # Rename columns to database field names
            df = df.rename(
                columns=column_mapping
            )  # Handle special case: "type" column is always expected but might be mapped as wire_set_group
            if "wire_set_group" not in df.columns and "type" in df.columns:
                # Map the 'type' column to wire_set_group as fallback
                df = df.rename(columns={"type": "wire_set_group"})
                self.logger.info("Mapped 'type' column to 'wire_set_group'")

            # Check for required columns after mapping
            required_fields = ["serial_number"]
            missing_fields = [
                field for field in required_fields if field not in df.columns
            ]
            if missing_fields:
                self.logger.error(
                    f"Missing required columns after mapping: {missing_fields}"
                )
                self.logger.error(
                    f"Available columns after mapping: {df.columns.tolist()}"
                )
                return []

            # Make sure wire_set_group exists - if not, it may be in the type column
            if "wire_set_group" not in df.columns:
                self.logger.warning(
                    "No 'wire_set_group' column found. Available columns: "
                    f"{df.columns.tolist()}"
                )
                # Continue anyway, we'll try to use the type column below

            # Filter out rows with missing required data
            initial_count = len(df)
            df = df.dropna(subset=["serial_number"])
            filtered_count = len(df)
            if initial_count != filtered_count:
                self.logger.info(
                    f"Filtered out {initial_count - filtered_count} rows with missing serial numbers"
                )

            self.logger.info(f"Processing {len(df)} rows with valid required fields")

            validated_records = []
            validation_errors = []  # Process each row through the schema
            for idx, row in df.iterrows():

                try:

                    # 1. turn the Series into a dict
                    row_dict = row.to_dict()

                    # 2. create the schema
                    schema = WireSetCertSchema()

                    # 3. load (validate + deserialize) your data
                    result = schema.load(row_dict)

                    validated_records.append(result)

                except ValidationError as ve:
                    validation_errors.append(
                        {
                            "row": idx
                            + 2,  # +2 because pandas is 0-indexed and Excel starts at row 1 with headers
                            "errors": ve.messages,
                            "data": row_dict,
                        }
                    )
                    self.logger.warning(
                        f"Validation error in row {idx + 2}: {ve.messages}"
                    )
                    self.logger.debug(f"Row data that failed validation: {row_dict}")

                except Exception as e:
                    self.logger.warning(f"Error processing row {idx + 2}: {e}")
                    continue

            # Log summary
            total_processed = len(validated_records) + len(validation_errors)
            if validation_errors:
                self.logger.warning(
                    f"Excel parsing completed: {len(validation_errors)} rows had validation errors, "
                    f"{len(validated_records)} rows processed successfully out of {total_processed} total"
                )
            else:
                self.logger.info(
                    f"Excel parsing completed successfully: {len(validated_records)} records validated"
                )

            # Log examples for debugging
            if validated_records:
                self.logger.info(f"Example validated records: {validated_records[:2]}")

            return validated_records

        except Exception as e:
            self.logger.error(f"Error parsing WireSetCerts.xlsx with pandas: {e}")
            return []

    def _map_headers_to_fields(self, headers: List[str]) -> Dict[str, int]:
        """
        Map Excel headers to database field names using exact header matching.

        Args:
            headers: List of normalized header strings from Excel

        Returns:
            Dictionary mapping field names to column indices
        """
        column_mapping = {}

        # Normalize the headers we received
        normalized_headers = [header.strip().lower() for header in headers]

        # Map each expected Excel header to its column index
        for excel_header in self.excel_headers:
            normalized_excel_header = excel_header.lower()

            # Find the column index for this header
            for i, actual_header in enumerate(normalized_headers):
                if normalized_excel_header == actual_header:
                    # Map to the database field name
                    db_field = self.header_to_field_mapping[excel_header]
                    column_mapping[db_field] = i
                    self.logger.debug(
                        f"Mapped '{actual_header}' -> {db_field} (col {i})"
                    )
                    break
            else:
                # Header not found - log as warning but continue
                self.logger.warning(
                    f"Expected Excel header '{excel_header}' not found in sheet"
                )

        self.logger.info(f"Column mapping found: {column_mapping}")
        return column_mapping

    def _validate_required_columns(
        self, column_mapping: Dict[str, int], sheet_name: str
    ) -> bool:
        """
        Validate that required columns are present in the mapping.

        Args:
            column_mapping: Dictionary of field names to column indices
            sheet_name: Name of the sheet being processed

        Returns:
            True if required columns are present, False otherwise
        """
        required_fields = ["serial_number", "wire_set_group"]
        missing_fields = [
            field for field in required_fields if field not in column_mapping
        ]

        if missing_fields:
            self.logger.warning(
                f"Could not find required columns {missing_fields} in sheet '{sheet_name}'. "
                f"Found columns: {list(column_mapping.keys())}"
            )
            return False

        return True

    def _process_sheet_rows(
        self, sheet, column_mapping: Dict[str, int], sheet_name: str
    ) -> List[Dict[str, Any]]:
        """
        Process all data rows in a sheet and validate using schema.

        Args:
            sheet: Excel worksheet object
            column_mapping: Dictionary mapping field names to column indices
            sheet_name: Name of the sheet being processed

        Returns:
            List of validated record dictionaries
        """
        validated_records = []
        validation_errors = []

        for row_num in range(2, sheet.max_row + 1):
            try:
                row_data = list(
                    sheet.iter_rows(min_row=row_num, max_row=row_num, values_only=True)
                )[0]

                # Extract raw record from row
                raw_record = self._extract_raw_record(row_data, column_mapping)

                # Skip rows without required fields
                if not raw_record.get("serial_number") or not raw_record.get(
                    "wire_set_group"
                ):
                    continue

                # Validate and clean using schema
                try:
                    validated_record = self.schema.load(raw_record)
                    validated_records.append(validated_record)

                except ValidationError as ve:
                    # Log validation error but don't stop processing
                    validation_errors.append(
                        {"row": row_num, "errors": ve.messages, "data": raw_record}
                    )
                    self.logger.warning(
                        f"Validation error in row {row_num} of sheet '{sheet_name}': {ve.messages}"
                    )

            except (IndexError, TypeError) as e:
                self.logger.warning(
                    f"Error processing row {row_num} in sheet '{sheet_name}': {e}"
                )
                continue

        # Log summary of validation errors
        if validation_errors:
            self.logger.warning(
                f"Sheet '{sheet_name}': {len(validation_errors)} rows had validation errors, "
                f"{len(validated_records)} rows processed successfully"
            )

        return validated_records

    def _extract_raw_record(
        self, row_data: tuple, column_mapping: Dict[str, int]
    ) -> Dict[str, Any]:
        """
        Extract a raw record dictionary from Excel row data.

        Args:
            row_data: Tuple of cell values from Excel row
            column_mapping: Dictionary mapping field names to column indices

        Returns:
            Dictionary with raw field values
        """
        record: Dict[str, Any] = {}

        for field_name, col_index in column_mapping.items():
            if col_index < len(row_data):
                raw_value = row_data[col_index]
                record[field_name] = self._parse_field_value(field_name, raw_value)

        return record

    def _parse_field_value(self, field_name: str, raw_value: Any) -> Any:
        """
        Parse and convert a raw cell value based on the field type.

        Args:
            field_name: Name of the database field
            raw_value: Raw value from Excel cell

        Returns:
            Parsed value appropriate for the field type
        """
        if raw_value is None:
            return None

        # Handle datetime fields
        if field_name in ["service_date", "next_service_date"]:
            if isinstance(raw_value, datetime):
                return raw_value
            elif isinstance(raw_value, str) and raw_value.strip():
                # Try common date formats
                for date_format in [
                    "%Y-%m-%d",
                    "%m/%d/%Y",
                    "%d/%m/%Y",
                    "%Y-%m-%d %H:%M:%S",
                ]:
                    try:
                        return datetime.strptime(raw_value.strip(), date_format)
                    except ValueError:
                        continue
                self.logger.debug(
                    f"Could not parse date '{raw_value}' for field {field_name}"
                )
                return None
            return None

        # Handle integer fields
        elif field_name == "asset_id":
            if isinstance(raw_value, (int, float)):
                return int(raw_value)
            elif isinstance(raw_value, str) and raw_value.strip():
                try:
                    return int(float(raw_value.strip()))
                except (ValueError, TypeError):
                    return None
            return None

        # Handle string fields
        else:
            if isinstance(raw_value, str):
                stripped = raw_value.strip()
                return stripped if stripped else None
            elif raw_value is not None:
                return str(raw_value).strip()
            return None

    def _update_wire_set_certs_table(
        self, mappings: List[Dict[str, Any]]
    ) -> WireSetCertResult:
        """
        Update the wire_set_certs table with new mappings.

        Args:
            mappings: List of validated wire set certificate dictionaries

        Returns:
            Dict with update statistics
        """
        result = WireSetCertResult(
            status="success",
            message="",
            records_processed=0,
            records_added=0,
            records_updated=0,
            errors=[],
        )

        try:
            # Start a transaction
            for mapping in mappings:
                result.records_processed += 1

                # Check if record already exists
                existing = (
                    self.session.query(WireSetCert)
                    .filter_by(serial_number=mapping["serial_number"])
                    .first()
                )

                if existing:
                    # Update existing record if any field has changed
                    updated = self._update_existing_record(existing, mapping)
                    if updated:
                        result.records_updated += 1
                        self.logger.info(f"Updated serial {mapping['serial_number']}")
                else:
                    # Insert new record
                    self._insert_new_record(mapping)
                    result.records_added += 1
                    self.logger.info(
                        f"Added new serial {mapping['serial_number']}: {mapping['wire_set_group']}"
                    )

            # Commit the transaction
            self.session.commit()

            self.logger.info(
                f"Database update completed: "
                f"{result.records_added} added, "
                f"{result.records_updated} updated, "
                f"{result.records_processed} processed"
            )

        except Exception as e:
            # Rollback on error
            self.session.rollback()
            self.logger.error(f"Error updating wire_set_certs table: {e}")
            result.status = "error"
            result.message = f"Database update failed: {str(e)}"
            result.errors.append(str(e))

        return result

    def _update_existing_record(
        self, existing: WireSetCert, mapping: Dict[str, Any]
    ) -> bool:
        """
        Update an existing WireSetCert record with new data.

        Args:
            existing: Existing database record
            mapping: New data from Excel

        Returns:
            True if any field was updated, False otherwise
        """
        updated = False
        # List of fields that can be updated (excluding id, created_at, updated_at)
        updatable_fields = [
            "wire_set_group",
            "asset_id",
            "asset_tag",
            "custom_order_number",
            "service_date",
            "next_service_date",
            "certificate_number",
            "wire_roll_cert_number",
        ]

        for field_name in updatable_fields:
            new_value = mapping.get(field_name)
            current_value = getattr(existing, field_name, None)

            if new_value != current_value:
                setattr(existing, field_name, new_value)
                updated = True
                self.logger.debug(
                    f"Updated {field_name} for serial {mapping['serial_number']}: "
                    f"{current_value} -> {new_value}"
                )

        return updated

    def _insert_new_record(self, mapping: Dict[str, Any]) -> None:
        """
        Insert a new WireSetCert record into the database.

        Args:
            mapping: Validated data from Excel
        """
        new_cert = WireSetCert(
            serial_number=mapping["serial_number"],
            wire_set_group=mapping["wire_set_group"],
            asset_id=mapping.get("asset_id"),
            asset_tag=mapping.get("asset_tag"),
            custom_order_number=mapping.get("custom_order_number"),
            service_date=mapping.get("service_date"),
            next_service_date=mapping.get("next_service_date"),
            certificate_number=mapping.get("certificate_number"),
            wire_roll_cert_number=mapping.get("wire_roll_cert_number"),
        )
        self.session.add(new_cert)


def refresh_wire_set_certs() -> WireSetCertResult:
    """
    Convenience function to refresh wire set certificates.

    Returns:
        Dict containing refresh operation results
    """
    refresher = WireSetCertRefresher()
    try:
        return refresher.refresh_wire_set_certs()
    finally:
        refresher.session.close()

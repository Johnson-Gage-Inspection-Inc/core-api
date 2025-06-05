# utils/wire_set_cert_refresher.py
"""
Utility module for refreshing wire set certificate data from SharePoint.

TODO: This module should handle:
1. Downloading WireSetCerts.xlsx from SharePoint Pyro folder
2. Parsing the Excel file to extract serial number mappings
3. Updating the wire_set_certs database table
4. Providing refresh status and error reporting
"""

import logging
from typing import Dict, List, Optional

from sqlalchemy.orm import Session

from db.models import WireSetCert
from utils.database import SessionLocal
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

        # TODO: Configure these based on your SharePoint structure
        self.sharepoint_site = None  # Will be set from config
        self.pyro_folder_path = "Shared Documents/Pyro"  # TODO: Verify this path
        self.wiresetcerts_filename = "WireSetCerts.xlsx"

    def refresh_wire_set_certs(self) -> Dict:
        """
        Refresh wire set certificate data from SharePoint.

        Returns:
            Dict containing refresh operation results
        """
        result = {
            "status": "success",
            "message": "",
            "records_processed": 0,
            "records_added": 0,
            "records_updated": 0,
            "errors": [],
        }

        try:
            # Download the Excel file from SharePoint
            excel_data = self._download_wiresetcerts_file()

            if not excel_data:
                result["status"] = "error"
                result["message"] = "Failed to download WireSetCerts.xlsx"
                return result

            # Parse the Excel file
            wire_set_mappings = self._parse_wiresetcerts_excel(excel_data)

            if not wire_set_mappings:
                result["status"] = "warning"
                result["message"] = "No wire set mappings found in file"
                return result

            # Update the database
            update_result = self._update_wire_set_certs_table(wire_set_mappings)
            result.update(update_result)

            self.logger.info(f"Wire set cert refresh completed: {result}")

        except Exception as e:
            self.logger.error(f"Error during wire set cert refresh: {e}")
            result["status"] = "error"
            result["message"] = f"Refresh failed: {str(e)}"
            result["errors"].append(str(e))

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

    def _parse_wiresetcerts_excel(self, excel_data: bytes) -> List[Dict]:
        """
        Parse the WireSetCerts.xlsx file to extract serial number mappings.

        Args:
            excel_data: Raw Excel file content

        Returns:
            List of dictionaries with serial_number and wire_set_group mappings
        """
        try:
            import io

            from openpyxl import load_workbook

            # Load the Excel file from bytes
            workbook = load_workbook(io.BytesIO(excel_data), read_only=True)

            self.logger.info(
                f"Successfully loaded Excel file with sheets: {workbook.sheetnames}"
            )

            mappings = []

            # Process each sheet in the workbook
            for sheet_name in workbook.sheetnames:
                sheet = workbook[sheet_name]
                self.logger.info(
                    f"Processing sheet '{sheet_name}' with {sheet.max_row} rows"
                )

                if not sheet.max_row or sheet.max_row < 2:
                    self.logger.warning(f"Sheet '{sheet_name}' has no data rows")
                    continue

                # Get headers from first row
                headers_row = list(
                    sheet.iter_rows(min_row=1, max_row=1, values_only=True)
                )[0]
                headers = [
                    str(cell).strip().lower() if cell else "" for cell in headers_row
                ]

                self.logger.info(f"Sheet headers: {headers}")

                # Find columns for serial number and wire set group
                serial_col = None
                group_col = None

                # Look for common column names for serial numbers
                serial_keywords = [
                    "serial",
                    "serial_number",
                    "serial number",
                    "wire_serial",
                    "wire serial",
                ]

                for i, header in enumerate(headers):
                    if any(keyword in header for keyword in serial_keywords):
                        serial_col = i
                        break

                # Look for common column names for wire set groups
                group_keywords = [
                    "type",  # This is the actual column name in WireSetCerts.xlsx
                    "group",
                    "wire_set_group",
                    "wire set group",
                    "wire_set",
                    "wire set",
                    "set_group",
                    "set group",
                ]
                for i, header in enumerate(headers):
                    if any(keyword in header for keyword in group_keywords):
                        group_col = i
                        break

                if serial_col is None or group_col is None:
                    self.logger.warning(
                        f"Could not find required columns in sheet '{sheet_name}'. "
                        f"Serial column: {serial_col}, Group column: {group_col}"
                    )
                    continue

                # Process data rows
                for row_num in range(2, sheet.max_row + 1):
                    try:
                        row_data = list(
                            sheet.iter_rows(
                                min_row=row_num, max_row=row_num, values_only=True
                            )
                        )[0]

                        serial_number = (
                            row_data[serial_col] if serial_col < len(row_data) else None
                        )
                        wire_set_group = (
                            row_data[group_col] if group_col < len(row_data) else None
                        )

                        # Skip empty rows
                        if not serial_number or not wire_set_group:
                            continue

                        # Clean up the values
                        serial_number = str(serial_number).strip()
                        wire_set_group = str(wire_set_group).strip()

                        if serial_number and wire_set_group:
                            mappings.append(
                                {
                                    "serial_number": serial_number,
                                    "wire_set_group": wire_set_group,
                                }
                            )

                    except (IndexError, TypeError) as e:
                        self.logger.warning(
                            f"Error processing row {row_num} in sheet '{sheet_name}': {e}"
                        )
                        continue

            workbook.close()

            self.logger.info(
                f"Extracted {len(mappings)} wire set mappings from Excel file"
            )

            # Log a few examples for debugging
            if mappings:
                examples = mappings[:3]
                self.logger.info(f"Example mappings: {examples}")

            return mappings

        except Exception as e:
            self.logger.error(f"Error parsing WireSetCerts.xlsx: {e}")
            return []

    def _update_wire_set_certs_table(self, mappings: List[Dict]) -> Dict:
        """
        Update the wire_set_certs table with new mappings.

        Args:
            mappings: List of serial number to wire set group mappings

        Returns:
            Dict with update statistics
        """
        result = {
            "records_processed": 0,
            "records_added": 0,
            "records_updated": 0,
            "errors": [],
        }

        try:
            # Start a transaction
            for mapping in mappings:
                result["records_processed"] += 1

                # Check if record already exists
                existing = (
                    self.session.query(WireSetCert)
                    .filter_by(serial_number=mapping["serial_number"])
                    .first()
                )

                if existing:
                    # Update existing record if the wire_set_group has changed
                    if existing.wire_set_group != mapping["wire_set_group"]:
                        existing.wire_set_group = mapping["wire_set_group"]
                        result["records_updated"] += 1
                        self.logger.info(
                            f"Updated serial {mapping['serial_number']}: "
                            f"{existing.wire_set_group} -> {mapping['wire_set_group']}"
                        )
                else:
                    # Insert new record
                    new_cert = WireSetCert(
                        serial_number=mapping["serial_number"],
                        wire_set_group=mapping["wire_set_group"],
                    )
                    self.session.add(new_cert)
                    result["records_added"] += 1
                    self.logger.info(
                        f"Added new serial {mapping['serial_number']}: {mapping['wire_set_group']}"
                    )

            # Commit the transaction
            self.session.commit()

            self.logger.info(
                f"Database update completed: "
                f"{result['records_added']} added, "
                f"{result['records_updated']} updated, "
                f"{result['records_processed']} processed"
            )

        except Exception as e:
            # Rollback on error
            self.session.rollback()
            self.logger.error(f"Error updating wire_set_certs table: {e}")
            result["errors"].append(str(e))

        return result


def refresh_wire_set_certs() -> Dict:
    """
    Convenience function to refresh wire set certificates.

    TODO: This is the main entry point for the refresh operation.
    Called by the API endpoint to trigger the refresh.

    Returns:
        Dict containing refresh operation results
    """
    refresher = WireSetCertRefresher()
    try:
        return refresher.refresh_wire_set_certs()
    finally:
        refresher.session.close()


# TODO: Consider adding these additional functions:
# - validate_wire_set_mappings(mappings: List[Dict]) -> List[str]
# - get_wire_set_for_serial(serial_number: str) -> Optional[str]
# - export_wire_set_certs_to_csv() -> str
# - get_wire_set_for_serial(serial_number: str) -> Optional[str]
# - export_wire_set_certs_to_csv() -> str

# utils/wire_offset_refresher.py
"""
Wire offset refresh pipeline.
Handles downloading updated wire certificate files from SharePoint and updating the database.
"""

import logging
import os
from typing import Any, Dict, List, Optional

from office365.sharepoint.files.file import File
from sqlalchemy.orm import Session

from db.models import WireOffset
from integrations.sharepoint.client import get_pyro_standards_files
from utils.constants import wirecert_filename_pattern
from utils.database import SessionLocal
from utils.wire_offset_parser import parse_wire_offsets_from_excel


def refresh_wire_offsets(
    updated_files: Optional[List[File]] = None,
    session: Optional[Session] = None,
) -> Dict[str, Any]:
    """
    Refresh wire offset data from SharePoint.

    This function:
    1. Downloads updated wire certificate files (.xls) from SharePoint
    2. Parses offset data from the Excel files using wire_offset_parser
    3. Upserts the data into the wire_offsets database table

    Args:
        updated_files: Optional list of file info dicts. If None, will check for recent updates.
        session: Optional database session (for testing)

    Returns:
        Dict containing refresh operation results with status, files processed, records added, etc.
    """
    logger = logging.getLogger(__name__)
    logger.info("Starting wire offset refresh")

    result = {
        "status": "success",
        "message": "",
        "files_processed": 0,
        "files_found": 0,
        "records_processed": 0,
        "records_added": 0,
        "records_updated": 0,
        "errors": [],
    }

    # Use provided session or create new one
    use_provided_session = session is not None
    if not use_provided_session:
        session = SessionLocal()

    try:  # If no files provided or empty list, get updated files from SharePoint
        if updated_files is None or len(updated_files) == 0:
            logger.info("No files provided, fetching updated wire certificate files")
            all_files = get_pyro_standards_files()

            # Filter for wire certificate files
            updated_files = []
            for file_obj in all_files:
                filename = file_obj.name
                if wirecert_filename_pattern.match(filename):
                    updated_files.append(file_obj)

        result["files_found"] = len(updated_files)

        if not updated_files:
            result["message"] = "No wire certificate files found to process"
            logger.info(result["message"])
            return result

        logger.info(
            f"Processing {len(updated_files)} wire certificate files"
        )  # Process each file
        for file_info in updated_files:
            filename = "unknown"  # Initialize filename for error handling
            try:
                # file_info is always a File object per type annotation
                filename = file_info.name
                file_obj = file_info

                logger.info(f"Processing wire certificate file: {filename}")

                if not file_obj:
                    error_msg = f"No file object available for: {filename}"
                    logger.error(error_msg)
                    result["errors"].append(error_msg)
                    continue

                # Download file content as bytes using native SDK
                try:
                    file_content = file_obj.get_content().value
                except Exception as download_error:
                    error_msg = f"Failed to download file {filename}: {download_error}"
                    logger.error(error_msg)
                    result["errors"].append(error_msg)
                    continue

                # Create temporary file for the parser (which expects a file path)
                import tempfile

                temp_dir = tempfile.gettempdir()
                temp_file_path = os.path.join(temp_dir, filename)

                with open(temp_file_path, "wb") as temp_file:
                    temp_file.write(file_content)

                # Parse wire offset data from the Excel file
                try:
                    offset_data = parse_wire_offsets_from_excel(temp_file_path)
                    logger.info(
                        f"Parsed {len(offset_data)} offset records from {filename}"
                    )

                    if not offset_data:
                        logger.warning(f"No offset data found in {filename}")
                        continue
                    # Extract traceability number from filename (e.g., "072513A.xls" -> "072513A")
                    traceability_no = os.path.splitext(filename)[0]

                    # Process each offset record
                    records_for_this_file = 0
                    for data in offset_data:
                        try:
                            # Map parsed data to database model
                            # Wire offset parser returns: {"TraceabilityNo", "NominalTemp", "CorrectionFactor"}
                            # Create new wire offset record using proper schema (append-only table)

                            # Get modified_by from file_info
                            modified_by = file_info.modified_by

                            wire_offset = WireOffset(
                                traceability_no=data.get(
                                    "TraceabilityNo", traceability_no
                                ),
                                nominal_temp=data["NominalTemp"],
                                correction_factor=data["CorrectionFactor"],
                                updated_by=modified_by,
                            )

                            session.add(wire_offset)
                            records_for_this_file += 1
                            result["records_added"] += 1

                        except Exception as e:
                            error_msg = (
                                f"Error processing offset record in {filename}: {e}"
                            )
                            logger.error(error_msg)
                            result["errors"].append(error_msg)
                            continue

                    result["records_processed"] += records_for_this_file
                    result["files_processed"] += 1
                    logger.info(
                        f"Successfully processed {records_for_this_file} records from {filename}"
                    )

                except Exception as e:
                    error_msg = f"Error parsing Excel file {filename}: {e}"
                    logger.error(error_msg)
                    result["errors"].append(error_msg)
                    continue

                finally:
                    # Clean up temporary file
                    try:
                        if temp_file_path and os.path.exists(temp_file_path):
                            os.remove(temp_file_path)
                    except Exception as e:
                        logger.warning(
                            f"Could not clean up temp file {temp_file_path}: {e}"
                        )

            except Exception as e:
                error_msg = f"Error processing file {filename}: {e}"
                logger.error(error_msg)
                result["errors"].append(error_msg)
                continue

        # Commit all changes
        session.commit()

        # Prepare final result message
        if result["errors"]:
            result["status"] = "partial_success"
            result["message"] = (
                f"Processed {result['files_processed']} files with {len(result['errors'])} errors"
            )
        else:
            result["message"] = (
                f"Successfully processed {result['files_processed']} files, {result['records_processed']} records"
            )

        logger.info(f"Wire offset refresh completed: {result['message']}")

    except Exception as e:
        # Rollback on major error
        session.rollback()
        error_msg = f"Wire offset refresh failed: {str(e)}"
        logger.error(error_msg)
        result["status"] = "error"
        result["message"] = error_msg
        result["errors"].append(str(e))

    finally:
        # Only close session if we created it (not provided by test)
        if not use_provided_session:
            session.close()

    return result

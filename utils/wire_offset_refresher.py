# utils/wire_offset_refresher.py
"""
Wire offset refresh pipeline.
Handles downloading updated wire certificate files from SharePoint and updating the database.
"""

import logging
import os
from typing import Any, Dict, List, Optional

from sqlalchemy.orm import Session

from db.models import WireOffset
from utils.constants import wirecert_filename_pattern
from utils.database import SessionLocal
from utils.sharepoint_client import SharePointClient
from utils.wire_offset_parser import parse_wire_offsets_from_excel


def refresh_wire_offsets(
    updated_files: Optional[List[Dict[str, Any]]] = None,
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

    try:
        # If no files provided, get updated files from SharePoint
        if updated_files is None:
            logger.info("No files provided, fetching updated wire certificate files")
            sharepoint_client = SharePointClient()
            all_files = sharepoint_client.list_files_in_pyro_standards_folder()

            # Filter for wire certificate files
            updated_files = []
            for file_info in all_files:
                filename = file_info.get("name", "")
                if wirecert_filename_pattern.match(filename):
                    updated_files.append(file_info)

        result["files_found"] = len(updated_files)

        if not updated_files:
            result["message"] = "No wire certificate files found to process"
            logger.info(result["message"])
            return result

        logger.info(f"Processing {len(updated_files)} wire certificate files")

        # Process each file
        for file_info in updated_files:
            try:
                filename = file_info.get("name", "")
                logger.info(f"Processing wire certificate file: {filename}")

                # Download the file
                file_path = SharePointClient.download_file_from_sharepoint(file_info)
                if not file_path or not os.path.exists(file_path):
                    error_msg = f"Failed to download file: {filename}"
                    logger.error(error_msg)
                    result["errors"].append(error_msg)
                    continue

                # Parse wire offset data from the Excel file
                try:
                    offset_data = parse_wire_offsets_from_excel(file_path)
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

                            wire_offset = WireOffset(
                                traceability_no=data.get(
                                    "TraceabilityNo", traceability_no
                                ),
                                nominal_temp=data["NominalTemp"],
                                correction_factor=data["CorrectionFactor"],
                                updated_by=file_info.get("modified_by", "SharePoint"),
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
                    # Clean up downloaded file
                    try:
                        if file_path and os.path.exists(file_path):
                            os.remove(file_path)
                    except Exception as e:
                        logger.warning(f"Could not clean up temp file {file_path}: {e}")

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

#!/usr/bin/env python
# utils/initialize_wire_offsets.py
"""
Initialize wire_offsets table with all historical data from SharePoint.

This script fetches all wire certificate files from the SharePoint Pyro Standards folder
and populates the wire_offsets table with all historical data.
"""

import logging
from typing import Any, Dict, List

from office365.sharepoint.files.file import File
from sqlalchemy import text

# Import config first to load environment variables
import config  # noqa: F401
from utils.database import SessionLocal
from utils.wire_offset_refresher import refresh_wire_offsets

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_all_wire_certificate_files() -> List[File]:
    """
    Fetch all wire certificate files from SharePoint Pyro Standards folder.

    Returns:
        List of File objects for all .xls and .xlsx files
    """
    try:
        # Get all Excel files from the Pyro Standards folder
        logger.info("Fetching all Excel files from SharePoint Pyro Standards folder...")
        from integrations.sharepoint import list_pyro_standards_excel_files

        all_excel_files = list_pyro_standards_excel_files()

        # Filter for wire certificate files (.xls and .xlsx)
        wire_cert_files = []
        for file_info in all_excel_files:
            filename = file_info.name
            if not filename:
                logger.warning("Found file with no name, skipping...")
                continue
            filename = filename.lower()
            if filename.endswith((".xls", ".xlsx")):
                wire_cert_files.append(file_info)
                logger.info(f"Found wire certificate file: {file_info.name}")

        logger.info(f"Found {len(wire_cert_files)} wire certificate files total")
        return wire_cert_files

    except Exception as e:
        logger.error(f"Error fetching wire certificate files: {e}")
        raise


def initialize_wire_offsets_table() -> Dict[str, Any]:
    """
    Initialize the wire_offsets table with all historical wire certificate data.

    Returns:
        Dictionary with initialization results and statistics
    """
    session = SessionLocal()

    try:
        # Check current state of the table

        count_before: int = (
            session.execute(text("SELECT COUNT(*) FROM public.wire_offsets")).scalar()
            or 0
        )

        logger.info(f"Records in wire_offsets before initialization: {count_before}")

        if count_before > 0:
            logger.warning(
                "Wire offsets table already has data. Use refresh instead of initialization."
            )
            response = input("Table already has data. Continue anyway? (y/N): ")
            if response.lower() != "y":
                return {
                    "status": "skipped",
                    "message": "Initialization skipped - table already has data",
                    "records_before": count_before,
                    "records_after": count_before,
                    "files_processed": 0,
                }
        # Clear any existing wire_offsets data
        logger.info("Clearing existing wire_offsets data...")
        session.execute(text("DELETE FROM public.wire_offsets"))

        # Note: refresh_log is a general log table, not table-specific
        # We'll add a new entry for this initialization rather than clearing old ones
        session.commit()

        # Get all wire certificate files from SharePoint
        wire_cert_files = get_all_wire_certificate_files()

        if not wire_cert_files:
            logger.warning("No wire certificate files found in SharePoint")
            return {
                "status": "no_files",
                "message": "No wire certificate files found in SharePoint",
                "records_before": count_before,
                "records_after": count_before,
                "files_processed": 0,
            }

        logger.info(f"Starting initialization with {len(wire_cert_files)} files...")

        # Process all files using the refresh_wire_offsets function
        result = refresh_wire_offsets(updated_files=wire_cert_files, session=session)

        # Check final state
        count_after: int = (
            session.execute(text("SELECT COUNT(*) FROM public.wire_offsets")).scalar()
            or 0
        )
        logger.info(f"Records in wire_offsets after initialization: {count_after}")

        # Check view state
        view_count: int = (
            session.execute(
                text("SELECT COUNT(*) FROM public.wire_offsets_current")
            ).scalar()
            or 0
        )
        logger.info(f"Records in wire_offsets_current view: {view_count}")

        # Get some sample records to verify data quality
        sample_records = session.execute(
            text(
                "SELECT id, traceability_no, nominal_temp, correction_factor FROM public.wire_offsets LIMIT 5"
            )
        ).fetchall()

        logger.info("Sample records inserted:")
        for record in sample_records:
            logger.info(
                f"  ID: {record[0]}, Traceability: {record[1]}, Temp: {record[2]}, Factor: {record[3]}"
            )

        return {
            "status": "success",
            "message": f"Successfully initialized wire_offsets table with {count_after} records",
            "records_before": count_before,
            "records_after": count_after,
            "records_added": count_after - count_before,
            "files_processed": len(wire_cert_files),
            "files_successful": result.get("successful_files", 0),
            "files_failed": result.get("failed_files", 0),
            "view_records": view_count,
            "sample_records": [
                dict(
                    zip(
                        ["id", "traceability_no", "nominal_temp", "correction_factor"],
                        record,
                    )
                )
                for record in sample_records
            ],
        }

    except Exception as e:
        logger.error(f"Error during initialization: {e}")
        session.rollback()
        raise
    finally:
        session.close()


def main():
    """Main entry point for the initialization script."""
    try:
        logger.info("Starting wire_offsets table initialization...")
        result = initialize_wire_offsets_table()

        print("\n" + "=" * 60)
        print("WIRE OFFSETS INITIALIZATION COMPLETE")
        print("=" * 60)
        print(f"Status: {result['status']}")
        print(f"Message: {result['message']}")
        print(f"Records before: {result['records_before']}")
        print(f"Records after: {result['records_after']}")
        print(f"Records added: {result.get('records_added', 0)}")
        print(f"Files processed: {result['files_processed']}")
        print(f"Files successful: {result.get('files_successful', 0)}")
        print(f"Files failed: {result.get('files_failed', 0)}")
        print(f"View records: {result.get('view_records', 0)}")

        if result.get("sample_records"):
            print("\nSample records:")
            for record in result["sample_records"]:
                print(f"  {record}")

        print("=" * 60)

    except Exception as e:
        logger.error(f"Initialization failed: {e}")
        print(f"\nERROR: Initialization failed - {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())

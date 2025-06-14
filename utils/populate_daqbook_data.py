#!/usr/bin/env python3
"""
Script to populate DAQbook offset data from SharePoint calibration files.

This script searches for DAQbook calibration files (.xlsm) on SharePoint
and extracts offset data to populate the daqbook_offsets table.

File patterns: J1_*, J2_*, J3_*, K4_*, K5_*, K6_*, N2_*.xlsm
"""

import os
import re
import sys
from typing import Dict, List, Optional

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import config to load environment variables
import config  # noqa: F401
from db.models import DaqbookOffset
from integrations.sharepoint import Office365SharePointClient


class DaqbookDataPopulator:
    """Populates DAQbook offset data from SharePoint calibration files."""

    def __init__(self):
        """Initialize the populator with database and SharePoint connections."""
        self.database_url = os.getenv("DATABASE_URL")
        if not self.database_url:
            raise ValueError("DATABASE_URL environment variable not set")

        self.engine = create_engine(self.database_url)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # Initialize SharePoint client
        self.sharepoint = Office365SharePointClient()

        # DAQbook file patterns
        self.daqbook_patterns = [
            r"^J1_.*\.xlsm$",
            r"^J2_.*\.xlsm$",
            r"^J3_.*\.xlsm$",
            r"^K4_.*\.xlsm$",
            r"^K5_.*\.xlsm$",
            r"^K6_.*\.xlsm$",
            r"^N2_.*\.xlsm$",
        ]

    def extract_tn_from_filename(self, filename: str) -> Optional[str]:
        """
        Extract test number (TN) from DAQbook filename.

        Args:
            filename: The filename (e.g., "J1_0325.xlsm")

        Returns:
            Test number (e.g., "J10325") or None if not matched
        """
        # Match patterns like J1_0325.xlsm -> J10325
        match = re.match(r"^([JKN])(\d+)_(\d+)\.xlsm$", filename)
        if match:
            prefix = match.group(1)
            series = match.group(2)
            number = match.group(3)
            return f"{prefix}{series}{number}"

        return None

    def search_daqbook_files(self) -> List[Dict]:
        """
        Search SharePoint for DAQbook calibration files.

        Returns:
            List of file information dictionaries
        """
        print("🔍 Searching SharePoint for DAQbook calibration files...")

        all_files = []

        for pattern in self.daqbook_patterns:
            try:
                print(f"   Searching for pattern: {pattern}")

                # Search for files matching the pattern
                search_results = self.sharepoint.search_files(
                    pattern.replace("^", "").replace("$", "")
                )

                for file_info in search_results:
                    filename = file_info.get("name", "")
                    if re.match(pattern, filename, re.IGNORECASE):
                        all_files.append(file_info)
                        print(f"   ✅ Found: {filename}")

            except Exception as e:
                print(f"   ❌ Error searching pattern {pattern}: {e}")
                continue

        print(f"📊 Total DAQbook files found: {len(all_files)}")
        return all_files

    def parse_daqbook_excel(self, file_content: bytes, tn: str) -> List[Dict]:
        """
        Parse DAQbook Excel file to extract offset data.

        Args:
            file_content: Raw Excel file content
            tn: Test number (e.g., "J10325")

        Returns:
            List of offset data dictionaries
        """
        print(f"📊 Parsing Excel data for {tn}...")

        try:
            # Read Excel file from bytes
            df = pd.read_excel(file_content, engine="openpyxl")

            offset_data = []

            # Look for temperature columns and point data
            # This is a simplified parser - adjust based on actual file structure
            temp_columns = []
            for col in df.columns:
                if isinstance(col, (int, float)) or (
                    isinstance(col, str)
                    and col.replace("-", "").replace(".", "").isdigit()
                ):
                    temp_columns.append(col)

            print(f"   Temperature columns found: {temp_columns}")

            # Extract data for each temperature point

            point_num = 0
            for _, row in df.iterrows():
                if pd.isna(row.iloc[0]):  # Skip empty rows
                    continue

                point_num += 1

                for temp_col in temp_columns:
                    temp_value = (
                        float(temp_col)
                        if isinstance(temp_col, (int, float))
                        else float(temp_col)
                    )
                    reading_value = row[temp_col]

                    if pd.notna(reading_value) and isinstance(
                        reading_value, (int, float)
                    ):
                        offset_data.append(
                            {
                                "tn": tn,
                                "temp": temp_value,
                                "point": point_num,
                                "reading": float(reading_value),
                            }
                        )

            print(f"   ✅ Extracted {len(offset_data)} data points")
            return offset_data

        except Exception as e:
            print(f"   ❌ Error parsing Excel file for {tn}: {e}")
            return []

    def save_offset_data(self, offset_data: List[Dict]) -> int:
        """
        Save offset data to database.

        Args:
            offset_data: List of offset data dictionaries

        Returns:
            Number of records saved
        """
        if not offset_data:
            return 0

        saved_count = 0

        for data in offset_data:
            try:
                # Check if record already exists
                existing = (
                    self.session.query(DaqbookOffset)
                    .filter_by(tn=data["tn"], temp=data["temp"], point=data["point"])
                    .first()
                )

                if existing:
                    # Update existing record
                    existing.reading = data["reading"]
                else:
                    # Create new record
                    offset_record = DaqbookOffset(**data)
                    self.session.add(offset_record)

                saved_count += 1

            except Exception as e:
                print(f"   ❌ Error saving record {data}: {e}")
                continue

        try:
            self.session.commit()
            print(f"   ✅ Saved {saved_count} offset records to database")
            return saved_count
        except Exception as e:
            self.session.rollback()
            print(f"   ❌ Error committing to database: {e}")
            return 0

    def process_daqbook_file(self, file_info: Dict) -> int:
        """
        Process a single DAQbook file.

        Args:
            file_info: File information from SharePoint search

        Returns:
            Number of records processed
        """
        filename = file_info.get("name", "")
        file_id = file_info.get("id", "")

        print(f"\n📄 Processing file: {filename}")

        # Extract test number from filename
        tn = self.extract_tn_from_filename(filename)
        if not tn:
            print(f"   ❌ Could not extract TN from filename: {filename}")
            return 0

        print(f"   📋 Test Number: {tn}")

        try:
            # Download file content
            print("   ⬇️ Downloading file content...")
            file_content = self.sharepoint.download_file_content(file_id)

            # Parse Excel data
            offset_data = self.parse_daqbook_excel(file_content, tn)

            # Save to database
            saved_count = self.save_offset_data(offset_data)

            return saved_count

        except Exception as e:
            print(f"   ❌ Error processing file {filename}: {e}")
            return 0

    def populate_all_daqbook_data(self) -> Dict[str, int]:
        """
        Main method to populate all DAQbook data.

        Returns:
            Dictionary with processing statistics
        """
        print("🚀 Starting DAQbook data population...")

        # Search for files
        daqbook_files = self.search_daqbook_files()

        if not daqbook_files:
            print("❌ No DAQbook files found on SharePoint")
            return {"files_found": 0, "files_processed": 0, "total_records": 0}

        # Process each file
        total_records = 0
        files_processed = 0

        for file_info in daqbook_files:
            try:
                records_saved = self.process_daqbook_file(file_info)
                if records_saved > 0:
                    files_processed += 1
                    total_records += records_saved
            except Exception as e:
                print(f"❌ Error processing file: {e}")
                continue

        # Final summary
        stats = {
            "files_found": len(daqbook_files),
            "files_processed": files_processed,
            "total_records": total_records,
        }

        print("\n🎉 DAQbook data population completed!")
        print(f"   📁 Files found: {stats['files_found']}")
        print(f"   ✅ Files processed: {stats['files_processed']}")
        print(f"   📊 Total records: {stats['total_records']}")

        return stats

    def close(self):
        """Close database connection."""
        self.session.close()


def main():
    """Main entry point."""
    try:
        populator = DaqbookDataPopulator()
        stats = populator.populate_all_daqbook_data()
        populator.close()

        if stats["files_processed"] > 0:
            print("\n✅ Successfully populated DAQbook data!")
            sys.exit(0)
        else:
            print("\n❌ No files were successfully processed")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

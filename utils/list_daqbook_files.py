#!/usr/bin/env python3
"""
Simple script to list DAQbook files on SharePoint and understand their structure.
"""

import os
import re
import sys

# Import config to load environment variables
import config  # noqa: F401
from integrations.sharepoint import Office365SharePointClient

# Add the parent directory to Python path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def search_daqbook_files():
    """Search for DAQbook calibration files on SharePoint."""

    print("🔍 Searching SharePoint for DAQbook calibration files...")

    # Initialize SharePoint client
    sharepoint = Office365SharePointClient()

    # Use the main drive ID for searching
    drive_id = sharepoint.drive_id
    if not drive_id:
        print("❌ SharePoint drive ID not configured")
        return []

    print(f"📂 Using drive ID: {drive_id}")

    # DAQbook file patterns
    patterns = ["J1_", "J2_", "J3_", "K4_", "K5_", "K6_", "N2_"]

    all_files = []

    for pattern in patterns:
        try:
            print(f"\n📂 Searching for files starting with '{pattern}'...")

            # Search for files
            search_results = sharepoint.search_files(f"{pattern}*.xlsm", drive_id)

            for file_info in search_results:
                filename = file_info.get("name", "")
                file_size = file_info.get("size", "Unknown")
                modified = file_info.get("lastModifiedDateTime", "Unknown")

                # Check if it matches our pattern
                if filename.lower().startswith(
                    pattern.lower()
                ) and filename.lower().endswith(".xlsm"):
                    # Add each file for each pattern it matches (allows duplicates)
                    all_files.append(file_info)
                    print(f"   ✅ {filename} (Size: {file_size}, Modified: {modified})")

        except Exception as e:
            print(f"   ❌ Error searching for '{pattern}': {e}")
            continue

    print("\n📊 Summary:")
    print(f"   Total DAQbook files found: {len(all_files)}")

    if all_files:
        print("\n📋 File list:")
        for i, file_info in enumerate(all_files, 1):
            filename = file_info.get("name", "")
            # Extract potential TN
            tn = extract_tn_from_filename(filename)
            print(f"   {i:2d}. {filename} → TN: {tn}")

    return all_files


def extract_tn_from_filename(filename: str) -> str:
    """Extract test number from filename."""
    # Try different patterns
    patterns = [
        r"^([JKN])(\d+)_(\d+)\.xlsm$",  # J1_0325.xlsm -> J10325
        r"^([JKN])(\d+)_(.+)\.xlsm$",  # More flexible
    ]

    for pattern in patterns:
        match = re.match(pattern, filename, re.IGNORECASE)
        if match:
            prefix = match.group(1).upper()
            series = match.group(2)
            number = match.group(3)
            return f"{prefix}{series}{number}"

    return "Unknown"


def main():
    """Main entry point."""
    try:
        files = search_daqbook_files()

        if files:
            print("\n🎯 Next steps:")
            print("   1. Review the file list above")
            print("   2. Check if TN extraction looks correct")
            print("   3. Run the full population script")
        else:
            print("\n❌ No DAQbook files found")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

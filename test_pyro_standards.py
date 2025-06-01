#!/usr/bin/env python3
"""
Test script for Pyro_Standards Excel file functionality.
Tests both getting specific files and listing all files in the Pyro_Standards folder.
"""

import config  # Load environment variables
from utils.sharepoint_client import (
    get_pyro_standards_excel_file,
    list_pyro_standards_excel_files,
)


def test_list_pyro_standards_files():
    """Test listing all Excel files in Pyro_Standards folder."""
    print("=== Testing list_pyro_standards_excel_files() ===")
    try:
        files = list_pyro_standards_excel_files()
        print(f"✅ Found {len(files)} Excel files in Pyro_Standards folder:")
        for file in files:
            print(f"  📄 {file['name']} ({file['size']} bytes)")
            print(f"     Last modified: {file['last_modified']}")
            print(f"     Web URL: {file['web_url']}")
            print()
        return files
    except Exception as e:
        print(f"❌ Error listing Pyro_Standards files: {e}")
        return []


def test_get_pyro_standards_excel_file(filename: str):
    """Test getting a specific Excel file from Pyro_Standards folder."""
    print(f"=== Testing get_pyro_standards_excel_file('{filename}') ===")
    try:
        result = get_pyro_standards_excel_file(filename)

        print(f"✅ Successfully retrieved '{filename}'")
        print("📊 File Info:")
        print(f"   Name: {result['file_info']['name']}")
        print(f"   Size: {result['file_info']['size']} bytes")
        print(f"   Last Modified: {result['file_info']['last_modified']}")
        print(f"   Web URL: {result['file_info']['web_url']}")
        print()

        print(f"📋 Sheets ({result['total_sheets']} total):")
        for sheet_name in result["sheet_names"]:
            sheet_data = result["sheets"][sheet_name]
            print(
                f"   '{sheet_name}': {sheet_data['total_rows']} rows × {sheet_data['total_columns']} columns"
            )

            if sheet_data["headers"]:
                print(f"     Headers: {sheet_data['headers']}")

            if sheet_data["sample_data"]:
                print(f"     Sample rows: {len(sheet_data['sample_data'])}")
                for i, row in enumerate(
                    sheet_data["sample_data"][:3]
                ):  # Show first 3 rows
                    print(f"       Row {i+2}: {row}")
            print()

        return result
    except Exception as e:
        print(f"❌ Error getting '{filename}': {e}")
        return None


def main():
    """Main test function."""
    print("🧪 Testing Pyro_Standards SharePoint Integration")
    print("=" * 50)

    # First, list all available files
    files = test_list_pyro_standards_files()

    if files:
        print("📝 Testing specific file retrieval...")
        # Test with the first Excel file found
        first_file = files[0]["name"]
        test_get_pyro_standards_excel_file(first_file)

        # Test with some common filenames that might exist
        common_files = [
            "K6_0824.xlsm",
            "calibration_data.xlsx",
            "pyro_K6_0824.xlsm",
            "Pyro K6_0824.xlsm",
        ]

        for filename in common_files:
            if filename != first_file:  # Don't test the same file twice
                matching_files = [
                    f for f in files if f["name"].lower() == filename.lower()
                ]
                if matching_files:
                    print(f"🔍 Testing file found in listing: {filename}")
                    test_get_pyro_standards_excel_file(filename)
                    break
    else:
        print("⚠️ No Excel files found in Pyro_Standards folder.")
        print("Testing with hypothetical filename...")
        test_get_pyro_standards_excel_file("K6_0824.xlsm")


if __name__ == "__main__":
    main()

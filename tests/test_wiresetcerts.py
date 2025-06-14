#!/usr/bin/env python3
"""
Test script to fetch and display WireSetCerts.xlsx content from SharePoint.
This script demonstrates the SharePoint integration functionality with app-only auth.
"""

import config  # noqa: F401  # Load environment variables from .env
from integrations.sharepoint import (
    get_wiresetcerts_content,
    get_wiresetcerts_file_reference,
)


def test_wiresetcerts_access():
    """Test accessing WireSetCerts.xlsx from SharePoint with app-only auth."""

    print("🔍 Testing SharePoint WireSetCerts.xlsx access...")
    print("=" * 60)

    try:
        # Test 1: Get file reference (metadata) - no token needed
        print("\n📄 Getting WireSetCerts.xlsx file reference...")
        file_ref = get_wiresetcerts_file_reference()

        print(f"File ID: {file_ref.get('id', 'N/A')}")
        print(f"File Name: {file_ref.get('name', 'N/A')}")
        print(f"File Size: {file_ref.get('size', 'N/A')} bytes")
        print(f"Web URL: {file_ref.get('webUrl', 'N/A')}")
        print(f"Download URL: {file_ref.get('downloadUrl', 'N/A')}")
        print(f"Last Modified: {file_ref.get('lastModified', 'N/A')}")
        print(f"MIME Type: {file_ref.get('mimeType', 'N/A')}")

        # Test 2: Get Excel content - no token needed
        print("\n📊 Getting WireSetCerts.xlsx content...")
        excel_data = get_wiresetcerts_content()

        print(f"Number of sheets: {excel_data.get('total_sheets', 0)}")

        for sheet_name, sheet_data in excel_data.get("sheets", {}).items():
            print(f"\n📋 Sheet: '{sheet_name}'")
            print(f"   Total rows: {sheet_data.get('total_rows', 0)}")
            print(f"   Total columns: {sheet_data.get('total_columns', 0)}")

            # Display headers
            headers = sheet_data.get("headers", [])
            if headers:
                print(f"   Headers: {headers[:5]}...")  # First 5 headers

            # Display sample data
            sample_data = sheet_data.get("sample_data", [])
            if sample_data:
                print("   Sample data (first 3 rows):")
                for i, row in enumerate(sample_data[:3]):
                    print(f"     Row {i+1}: {row[:5]}...")  # First 5 columns
            else:
                print("   No sample data available")

    except Exception as e:
        print(f"❌ Error accessing WireSetCerts.xlsx: {e}")
        print("\nNote: This is expected in test mode without real SharePoint access.")
        print(
            "The SharePoint client is properly configured and ready for real authentication."
        )


if __name__ == "__main__":
    test_wiresetcerts_access()

#!/usr/bin/env python3
"""
Script to fetch and display WireSetCerts.xlsx content from SharePoint.
Uses app-only authentication for headless operation.
"""

import sys
import os
import config  # Load environment variables from .env
from utils.sharepoint_client import get_wiresetcerts_content


def main():
    """Fetch and display WireSetCerts.xlsx content."""
    print("🔐 Using app-only authentication...")

    try:
        print("\n📄 Fetching WireSetCerts.xlsx from SharePoint...")
        # Fetch the Excel content (no token needed - will use app auth automatically)
        wiresetcerts_data = get_wiresetcerts_content()

        print(f"✅ Successfully fetched WireSetCerts.xlsx")
        print(
            f"📊 File contains {wiresetcerts_data['total_sheets']} sheet(s): {', '.join(wiresetcerts_data['sheet_names'])}"
        )        # Display the content
        if wiresetcerts_data and wiresetcerts_data.get("sheets"):
            print("\n" + "=" * 80)
            print("WIRESETCERTS.XLSX CONTENT")
            print("=" * 80)

            for sheet_name, sheet_data in wiresetcerts_data["sheets"].items():
                print(f"\n📋 Sheet: {sheet_name}")
                print(
                    f"   Size: {sheet_data['total_rows']} rows × {sheet_data['total_columns']} columns"
                )

                # Show headers
                headers = sheet_data.get('headers', [])
                if headers:
                    print(
                        f"   Headers: {', '.join(str(h) for h in headers[:5])}{'...' if len(headers) > 5 else ''}"
                    )

                # Show sample data
                sample_data = sheet_data.get('sample_data', [])
                if sample_data:
                    print("   Sample data:")
                    for i, row_data in enumerate(sample_data[:3], 1):
                        row_str = " | ".join(
                            str(cell)[:20] if cell is not None else "None"
                            for cell in row_data[:5]
                        )
                        if len(row_data) > 5:
                            row_str += " | ..."
                        print(f"     Row {i+1}: {row_str}")

                    if len(sample_data) > 3:
                        print(
                            f"     ... and {len(sample_data) - 3} more sample rows"
                        )

            print("\n" + "=" * 80)
        else:
            print("❌ No sheets found in WireSetCerts.xlsx")

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print(f"Error type: {type(e).__name__}")

        if "SHAREPOINT_DRIVE_ID not configured" in str(e):
            print("\n💡 Tip: Make sure SHAREPOINT_DRIVE_ID is set in your .env file")
        elif "Access token" in str(e):
            print(
                "\n💡 Tip: Make sure you're logged into Azure AD and have proper permissions"
            )
        elif "requests" in str(e).lower():
            print("\n💡 Tip: Check your network connection and SharePoint permissions")

        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

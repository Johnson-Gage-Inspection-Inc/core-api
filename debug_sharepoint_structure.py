#!/usr/bin/env python3
"""
Debug script to explore SharePoint drive structure and find WireSetCerts.xlsx.
Uses app-only authentication for headless operation.
"""

import sys
import os
import config  # Load environment variables from .env
from utils.sharepoint_client import SharePointClient


def explore_drive_structure():
    """Explore the SharePoint drive structure to find files."""
    try:
        print("🔐 Using app-only authentication...")
        client = SharePointClient()
        
        print(f"📂 Connected to SharePoint drive: {client.drive_id}")
        
        # Get root items
        print("\n📁 Root directory contents:")
        root_items = client.get_drive_items(client.drive_id)
        
        for item in root_items[:10]:  # Show first 10 items
            item_type = "📁" if item.get("folder") else "📄"
            name = item.get("name", "Unknown")
            size = item.get("size", 0)
            print(f"  {item_type} {name} ({size} bytes)")
        
        if len(root_items) > 10:
            print(f"  ... and {len(root_items) - 10} more items")
        
        # Search for WireSetCerts specifically
        print("\n🔍 Searching for WireSetCerts files...")
        search_results = client.search_files("WireSetCerts", client.drive_id)
        
        if search_results:
            print(f"Found {len(search_results)} matching files:")
            for file_info in search_results:
                name = file_info.get("name", "Unknown")
                path = file_info.get("parentReference", {}).get("path", "Unknown path")
                size = file_info.get("size", 0)
                file_id = file_info.get("id", "No ID")
                print(f"  📄 {name}")
                print(f"      Path: {path}")
                print(f"      Size: {size} bytes")
                print(f"      ID: {file_id}")
                print()
        else:
            print("No files found matching 'WireSetCerts'")
        
        # Try searching for .xlsx files
        print("\n🔍 Searching for Excel files (.xlsx)...")
        excel_results = client.search_files(".xlsx", client.drive_id)
        
        if excel_results:
            print(f"Found {len(excel_results)} Excel files:")
            for file_info in excel_results[:5]:  # Show first 5 Excel files
                name = file_info.get("name", "Unknown")
                path = file_info.get("parentReference", {}).get("path", "Unknown path")
                size = file_info.get("size", 0)
                print(f"  📄 {name}")
                print(f"      Path: {path}")
                print(f"      Size: {size} bytes")
                print()
            
            if len(excel_results) > 5:
                print(f"  ... and {len(excel_results) - 5} more Excel files")
        else:
            print("No Excel files found")
        
        print("\n✅ SharePoint exploration completed successfully!")
        
    except Exception as e:
        print(f"❌ Error exploring SharePoint: {e}")
        print(f"Error type: {type(e).__name__}")
        return False
    
    return True


def main():
    """Main function."""
    success = explore_drive_structure()
    
    if success:
        print("\n🎯 SharePoint app-only authentication is working!")
        print("The issue seems to be with the file location, not authentication.")
    else:
        print("\n⚠️  There may be an issue with SharePoint access or authentication.")
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())

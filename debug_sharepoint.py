#!/usr/bin/env python3
"""
Debug SharePoint configuration and access.
"""

import os
import requests
from utils.get_token import get_access_token


def main():
    """Debug SharePoint access."""
    print("🔍 SharePoint Configuration Debug")
    print("=" * 50)

    # Get access token
    print("🔐 Getting access token...")
    try:
        access_token = get_access_token()
        print("✅ Access token obtained")
    except Exception as e:
        print(f"❌ Failed to get access token: {e}")
        return 1

    headers = {"Authorization": f"Bearer {access_token}", "Accept": "application/json"}

    # Try to access known JGI SharePoint domain
    print("\n🔍 Trying to access JGI SharePoint sites...")
    jgi_domains = ["jgiquality.sharepoint.com", "johnsongageinspection.sharepoint.com"]

    for domain in jgi_domains:
        print(f"\n📋 Testing domain: {domain}")
        try:
            # Try root site
            root_url = f"https://graph.microsoft.com/v1.0/sites/{domain}"
            response = requests.get(root_url, headers=headers)
            if response.status_code == 200:
                site_data = response.json()
                print(f"✅ Root site found: {site_data.get('displayName', 'Unknown')}")
                print(f"   Site ID: {site_data.get('id', 'Unknown')}")

                # List drives in this site
                print("   📂 Checking drives...")
                drives_url = (
                    f"https://graph.microsoft.com/v1.0/sites/{site_data['id']}/drives"
                )
                drives_response = requests.get(drives_url, headers=headers)
                if drives_response.status_code == 200:
                    drives_data = drives_response.json()
                    print(f"   Found {len(drives_data.get('value', []))} drives:")
                    for drive in drives_data.get("value", []):
                        print(
                            f"     - {drive.get('name', 'Unknown')} (ID: {drive.get('id', 'Unknown')})"
                        )
                        print(f"       Type: {drive.get('driveType', 'Unknown')}")

                        # Check if this is the Pyro drive
                        if "pyro" in drive.get("name", "").lower():
                            print(f"       🎯 This looks like the Pyro drive!")

                            # Search for WireSetCerts.xlsx in this drive
                            print(f"       🔍 Searching for WireSetCerts.xlsx...")
                            search_url = f"https://graph.microsoft.com/v1.0/drives/{drive['id']}/root/search(q='WireSetCerts.xlsx')"
                            search_response = requests.get(search_url, headers=headers)
                            if search_response.status_code == 200:
                                search_data = search_response.json()
                                if search_data.get("value"):
                                    for file_item in search_data["value"]:
                                        print(
                                            f"       ✅ Found file: {file_item.get('name', 'Unknown')}"
                                        )
                                        print(
                                            f"          File ID: {file_item.get('id', 'Unknown')}"
                                        )
                                        print(
                                            f"          Path: {file_item.get('parentReference', {}).get('path', 'Unknown')}"
                                        )
                                else:
                                    print(
                                        f"       ❌ WireSetCerts.xlsx not found in this drive"
                                    )
                            else:
                                print(
                                    f"       ❌ Search failed: {search_response.status_code}"
                                )

            else:
                print(f"❌ Root site access failed: {response.status_code}")

        except Exception as e:
            print(f"❌ Error accessing {domain}: {e}")

    # Try specific Pyro site URL if known
    print(f"\n🔍 Trying known Pyro site URL...")
    try:
        pyro_site_url = "https://graph.microsoft.com/v1.0/sites/jgiquality.sharepoint.com:/sites/pyro"
        response = requests.get(pyro_site_url, headers=headers)
        if response.status_code == 200:
            site_data = response.json()
            print(f"✅ Pyro site found: {site_data.get('displayName', 'Unknown')}")
            print(f"   Site ID: {site_data.get('id', 'Unknown')}")

            # Get drives
            drives_url = (
                f"https://graph.microsoft.com/v1.0/sites/{site_data['id']}/drives"
            )
            drives_response = requests.get(drives_url, headers=headers)
            if drives_response.status_code == 200:
                drives_data = drives_response.json()
                print(f"   Found {len(drives_data.get('value', []))} drives:")
                for drive in drives_data.get("value", []):
                    print(
                        f"     - {drive.get('name', 'Unknown')} (ID: {drive.get('id', 'Unknown')})"
                    )

        else:
            print(f"❌ Pyro site access failed: {response.status_code}")

    except Exception as e:
        print(f"❌ Error accessing Pyro site: {e}")

    return 0


if __name__ == "__main__":
    exit(main())

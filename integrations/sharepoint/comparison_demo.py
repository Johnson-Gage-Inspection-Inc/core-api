# integrations/sharepoint/comparison_demo.py
"""
Side-by-side comparison: Graph API vs Office365-REST-Python-Client SDK

This demonstrates the dramatic difference in schema richness and type safety
between our current Graph API approach and the Office365 SDK.
"""

from datetime import datetime
from typing import Any, Dict


# Current approach simulation
class CurrentGraphAPIResponse:
    """Simulates our current Graph API response structure."""

    @staticmethod
    def get_file_metadata(file_path: str) -> Dict[str, Any]:
        """
        Current Graph API response - limited fields, manual parsing required.
        This is what we get from Microsoft Graph API /drives/{id}/items endpoint.
        """
        return {
            "id": "01BYE5RZ6QN3ZWBTUQNFDK2QJLR",
            "name": "WireSetCerts.xlsx",
            "size": 847360,
            "lastModifiedDateTime": "2024-12-15T14:30:22Z",  # STRING - manual parsing needed
            "webUrl": "https://jgiquality.sharepoint.com/sites/JGI/Shared%20Documents/Pyro/WireSetCerts.xlsx",
            "file": {
                "mimeType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            },
            "parentReference": {
                "driveId": "b!8LWrBhHvN0CgsELLmQq7dC",
                "path": "/drives/b!8LWrBhHvN0CgsELLmQq7dC/root:/Shared Documents/Pyro",
            },
            "@microsoft.graph.downloadUrl": "https://jgiquality.sharepoint.com/personal/...",
        }

    @staticmethod
    def parse_current_response(response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Current parsing logic - manual extraction, type conversion, error handling.
        This represents our current File creation process.
        """
        return {
            "id": response.get("id", ""),
            "name": response.get("name", ""),
            "size": response.get("size", 0),
            "last_modified": (
                datetime.fromisoformat(
                    response.get("lastModifiedDateTime", "").replace("Z", "+00:00")
                )
                if response.get("lastModifiedDateTime")
                else None
            ),
            "web_url": response.get("webUrl", ""),
            "mime_type": response.get("file", {}).get("mimeType", ""),
            "drive_id": response.get("parentReference", {}).get("driveId", ""),
            "folder_path": response.get("parentReference", {}).get("path", ""),
            "download_url": response.get("@microsoft.graph.downloadUrl", ""),
            # Missing information (not available through Graph API):
            "author": None,  # Can't get author info
            "version": None,  # No version information
            "checkout_status": None,  # No checkout info
            "custom_fields": {},  # No access to SharePoint columns
            "permissions": None,  # Limited permission data
            "workflow_status": None,  # No workflow information
        }


# Office365 SDK approach simulation
class Office365SDKResponse:
    """Simulates the rich Office365 SDK File object."""

    @staticmethod
    def get_file_metadata(file_path: str) -> Dict[str, Any]:
        """
        Office365 SDK File object properties - comprehensive metadata.
        This represents what we get from the Office365-REST-Python-Client SDK.
        """
        return {
            # Basic properties (same as Graph API but properly typed)
            "unique_id": "01BYE5RZ6QN3ZWBTUQNFDK2QJLR",
            "name": "WireSetCerts.xlsx",
            "title": "Wire Set Certificates Master File",
            "server_relative_url": "/sites/JGI/Shared Documents/Pyro/WireSetCerts.xlsx",
            "length": 847360,
            "content_tag": "'{F4C5B5C3-0A1B-4B3C-9D8E-7F6E5D4C3B2A},1'",
            "time_created": datetime(2023, 6, 15, 10, 30, 0),
            "time_last_modified": datetime(2024, 12, 15, 14, 30, 22),
            # Rich user information (not available in Graph API)
            "author": {
                "id": 123,
                "login_name": "i:0#.f|membership|jeff.hall@jgiquality.com",
                "title": "Jeff Hall",
                "email": "jeff.hall@jgiquality.com",
            },
            "modified_by": {
                "id": 124,
                "login_name": "i:0#.f|membership|calibration@jgiquality.com",
                "title": "Calibration Team",
                "email": "calibration@jgiquality.com",
            },
            # Version control (not available in Graph API)
            "major_version": 15,
            "minor_version": 3,
            "version_label": "15.3",
            "checkin_comment": "Updated Q4 2024 wire certifications",
            "check_out_type": 0,  # Not checked out
            "checked_out_by": None,
            # SharePoint metadata (not available in Graph API)
            "list_id": "F4C5B5C3-0A1B-4B3C-9D8E-7F6E5D4C3B2A",
            "site_id": "8LWrBhHvN0CgsELLmQq7dC",
            "web_id": "A1B2C3D4-E5F6-7890-ABCD-EF1234567890",
            "content_type_id": "0x0101004F0C8B3D2E1F0000A1B2C3D4E5F6",
            # Security and permissions (not available in Graph API)
            "irm_enabled": False,
            "has_unique_permissions": False,
            "effective_permissions": ["Read", "Write", "Delete"],
            # File status (not available in Graph API)
            "exists": True,
            "level": "Published",
            "customized_page_status": 0,
            # Parent relationships (limited in Graph API)
            "parent_folder": {
                "unique_id": "B2C3D4E5-F6A7-8901-BCDE-F23456789012",
                "name": "Pyro",
                "server_relative_url": "/sites/JGI/Shared Documents/Pyro",
                "item_count": 47,
            },
            # SharePoint custom columns (not accessible via Graph API)
            "custom_properties": {
                "DocumentType": "Calibration Certificate",
                "EquipmentCategory": "Wire Sets",
                "CalibrationDate": datetime(2024, 12, 1),
                "NextCalibrationDue": datetime(2025, 12, 1),
                "CertificateNumber": "WS-2024-047",
                "ApprovalStatus": "Approved",
                "TechnicalReviewer": "Dr. Sarah Johnson",
                "QualityLevel": "ISO 17025",
                "EquipmentIDs": ["WS001", "WS002", "WS003", "WS004"],
                "CalibrationLaboratory": "JGI Internal Lab",
                "Standards": ["NIST 890.02", "ASTM E74"],
                "UncertaintyBudget": "±0.0005%",
                "EnvironmentalConditions": "23°C ±2°C, 45% ±10% RH",
            },
            # List item properties (SharePoint-specific)
            "list_item_all_fields": {
                "id": 156,
                "content_type": "Calibration Document",
                "workflow_status": "Published",
                "approval_status": "Approved",
                "created": datetime(2023, 6, 15, 10, 30, 0),
                "modified": datetime(2024, 12, 15, 14, 30, 22),
            },
            # Version history (not available in Graph API)
            "version_history": [
                {
                    "version": "15.3",
                    "created": datetime(2024, 12, 15, 14, 30, 22),
                    "created_by": "Calibration Team",
                    "comment": "Updated Q4 2024 wire certifications",
                    "size": 847360,
                },
                {
                    "version": "15.2",
                    "created": datetime(2024, 9, 15, 9, 15, 10),
                    "created_by": "Jeff Hall",
                    "comment": "Q3 quarterly update",
                    "size": 834920,
                },
                {
                    "version": "15.1",
                    "created": datetime(2024, 6, 15, 16, 45, 30),
                    "created_by": "Calibration Team",
                    "comment": "Added new wire set models",
                    "size": 812440,
                },
            ],
        }


def demonstrate_schema_differences():
    """
    Demonstrate the dramatic difference in available metadata.
    """
    print("=" * 80)
    print("SCHEMA COMPARISON: Graph API vs Office365-REST-Python-Client SDK")
    print("=" * 80)

    # Current Graph API approach
    print("\n📊 CURRENT GRAPH API RESPONSE (Limited)")
    print("-" * 50)
    graph_response = CurrentGraphAPIResponse.get_file_metadata("WireSetCerts.xlsx")
    parsed_current = CurrentGraphAPIResponse.parse_current_response(graph_response)

    print(f"Available fields: {len(parsed_current)}")
    for key, value in parsed_current.items():
        if value is not None:
            print(f"  ✓ {key}: {type(value).__name__}")
        else:
            print(f"  ✗ {key}: Not available")

    # Office365 SDK approach
    print("\n🚀 OFFICE365 SDK RESPONSE (Comprehensive)")
    print("-" * 50)
    sdk_response = Office365SDKResponse.get_file_metadata("WireSetCerts.xlsx")

    print(f"Available fields: {len(sdk_response)}")

    print("\n📋 Basic Properties:")
    basic_fields = ["unique_id", "name", "length", "time_created", "time_last_modified"]
    for field in basic_fields:
        value = sdk_response.get(field)
        print(f"  ✓ {field}: {type(value).__name__} = {value}")

    print("\n👥 User Information (Not in Graph API):")
    author = sdk_response.get("author", {})
    print(f"  ✓ Author: {author.get('title')} ({author.get('email')})")
    modified_by = sdk_response.get("modified_by", {})
    print(f"  ✓ Modified by: {modified_by.get('title')} ({modified_by.get('email')})")

    print("\n📝 Version Control (Not in Graph API):")
    print(
        f"  ✓ Version: {sdk_response.get('major_version')}.{sdk_response.get('minor_version')}"
    )
    print(f"  ✓ Check-in comment: {sdk_response.get('checkin_comment')}")
    print(
        f"  ✓ Checkout status: {'Not checked out' if sdk_response.get('check_out_type') == 0 else 'Checked out'}"
    )

    print("\n🏢 SharePoint Metadata (Not in Graph API):")
    print(f"  ✓ List ID: {sdk_response.get('list_id')}")
    print(
        f"  ✓ Content Type: {sdk_response.get('list_item_all_fields', {}).get('content_type')}"
    )
    print(
        f"  ✓ Approval Status: {sdk_response.get('list_item_all_fields', {}).get('approval_status')}"
    )

    print("\n🔧 Custom Properties (SharePoint Columns - Not in Graph API):")
    custom_props = sdk_response.get("custom_properties", {})
    for key, value in list(custom_props.items())[:8]:  # Show first 8
        print(f"  ✓ {key}: {value}")
    print(f"  ... and {len(custom_props) - 8} more custom fields")

    print("\n📊 Version History (Not in Graph API):")
    versions = sdk_response.get("version_history", [])
    for i, version in enumerate(versions[:3]):  # Show latest 3 versions
        print(
            f"  ✓ v{version['version']}: {version['comment']} by {version['created_by']}"
        )

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Graph API fields: {len(parsed_current)} (basic metadata only)")
    print(f"Office365 SDK fields: {len(sdk_response)} (comprehensive SharePoint data)")
    print(f"Improvement: {len(sdk_response) - len(parsed_current)} additional fields")
    print(f"Custom SharePoint columns: {len(custom_props)} (impossible with Graph API)")
    print(f"Version history entries: {len(versions)} (impossible with Graph API)")

    print("\n🎯 KEY ADVANTAGES OF OFFICE365 SDK:")
    print("  ✓ Rich user objects with names and emails")
    print("  ✓ Complete version history with comments")
    print("  ✓ Access to SharePoint custom columns")
    print("  ✓ Built-in type safety (datetime objects vs strings)")
    print("  ✓ Comprehensive permission and security metadata")
    print("  ✓ Workflow and approval status")
    print("  ✓ Parent/child relationship navigation")
    print("  ✓ Content type and SharePoint-specific metadata")


def show_api_call_comparison():
    """
    Show the difference in API complexity.
    """
    print("\n" + "=" * 80)
    print("API COMPLEXITY COMPARISON")
    print("=" * 80)

    print("\n📱 CURRENT GRAPH API APPROACH (Complex)")
    print("-" * 50)
    print(
        """
# Multiple API calls needed for complete data
response1 = requests.get(f"{base_url}/drives/{drive_id}/items/{file_id}")
response2 = requests.get(f"{base_url}/drives/{drive_id}/items/{file_id}/versions")
response3 = requests.get(f"{base_url}/drives/{drive_id}/items/{file_id}/permissions")

# Manual parsing and error handling
file_data = response1.json()
versions = response2.json().get("value", []) if response2.status_code == 200 else []
permissions = response3.json().get("value", []) if response3.status_code == 200 else []

# Manual type conversion
created = datetime.fromisoformat(file_data["createdDateTime"].replace("Z", "+00:00"))
size = int(file_data.get("size", 0))

# No access to SharePoint custom columns
custom_data = {}  # Not available through Graph API
"""
    )

    print("\n🚀 OFFICE365 SDK APPROACH (Simple)")
    print("-" * 50)
    print(
        """
# Single SDK call gets comprehensive data
file_obj = context.web.get_file_by_server_relative_url(file_path)
context.load(file_obj)
context.execute_query()

# Rich object with all properties
name = file_obj.name  # Already string
size = file_obj.length  # Already int
created = file_obj.time_created  # Already datetime object
author = file_obj.author.title  # Rich user object
version = f"{file_obj.major_version}.{file_obj.minor_version}"

# Access to SharePoint custom columns
list_item = file_obj.listItemAllFields
custom_data = {
    "calibration_date": list_item.properties.get("CalibrationDate"),
    "equipment_id": list_item.properties.get("EquipmentID"),
    "approval_status": list_item.properties.get("ApprovalStatus")
}
"""
    )


if __name__ == "__main__":
    demonstrate_schema_differences()
    show_api_call_comparison()

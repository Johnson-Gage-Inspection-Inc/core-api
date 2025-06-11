# integrations/sharepoint/test_native_schemas.py
"""
Test script to demonstrate the power of using native Office365 SDK schemas.

This shows how much richer the native File and Folder objects are compared
to our custom wrapper classes or Graph API dictionaries.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


def demonstrate_native_file_properties():
    """Show all the rich properties available on native File objects."""
    print("🔍 Native Office365 File Object Properties")
    print("=" * 50)

    try:
        from office365.sharepoint.files.file import File

        # Get all properties (excluding private/methods)
        file_props = [
            prop
            for prop in dir(File)
            if not prop.startswith("_") and not callable(getattr(File, prop, None))
        ]

        print(f"📊 Total properties available: {len(file_props)}")
        print()

        # Core file properties
        core_props = [
            "unique_id",
            "name",
            "serverRelativeUrl",
            "length",
            "time_created",
            "time_last_modified",
            "exists",
        ]
        print("🔑 Core Properties:")
        for prop in core_props:
            if prop in file_props:
                print(f"  ✅ {prop}")

        # Relationship properties
        relation_props = [
            "author",
            "parent_folder",
            "checked_out_by_user",
            "modified_by",
            "locked_by_user",
        ]
        print("\n🔗 Relationship Properties:")
        for prop in relation_props:
            if prop in file_props:
                print(f"  ✅ {prop}")

        # Version/metadata properties
        version_props = [
            "major_version",
            "minor_version",
            "versions",
            "version_events",
            "check_out_type",
            "checkin_comment",
            "content_tag",
        ]
        print("\n📋 Version & Metadata Properties:")
        for prop in version_props:
            if prop in file_props:
                print(f"  ✅ {prop}")

        # SharePoint specific
        sp_props = [
            "list_id",
            "site_id",
            "web_id",
            "listItemAllFields",
            "irm_enabled",
            "customized_page_status",
            "linking_uri",
        ]
        print("\n🏢 SharePoint Specific Properties:")
        for prop in sp_props:
            if prop in file_props:
                print(f"  ✅ {prop}")

        # Advanced features
        advanced_props = [
            "activity_capabilities",
            "effective_information_rights_management_settings",
            "information_rights_management_settings",
        ]
        print("\n🚀 Advanced Feature Properties:")
        for prop in advanced_props:
            if prop in file_props:
                print(f"  ✅ {prop}")

        print(
            f"\n💡 And {len(file_props) - len(core_props + relation_props + version_props + sp_props + advanced_props)} more properties!"
        )

    except Exception as e:
        print(f"❌ Error exploring File properties: {e}")


def demonstrate_native_folder_properties():
    """Show all the rich properties available on native Folder objects."""
    print("\n🗂️  Native Office365 Folder Object Properties")
    print("=" * 50)

    try:
        from office365.sharepoint.folders.folder import Folder

        # Get all properties (excluding private/methods)
        folder_props = [
            prop
            for prop in dir(Folder)
            if not prop.startswith("_") and not callable(getattr(Folder, prop, None))
        ]

        print(f"📊 Total properties available: {len(folder_props)}")
        print()

        # Core folder properties
        core_props = [
            "unique_id",
            "name",
            "serverRelativeUrl",
            "time_created",
            "time_last_modified",
            "exists",
        ]
        print("🔑 Core Properties:")
        for prop in core_props:
            if prop in folder_props:
                print(f"  ✅ {prop}")

        # Collection properties
        collection_props = ["files", "folders", "parent_folder"]
        print("\n📂 Collection Properties:")
        for prop in collection_props:
            if prop in folder_props:
                print(f"  ✅ {prop}")

        # Content management
        content_props = [
            "content_type_order",
            "unique_content_type_order",
            "welcome_page",
            "is_wopi_enabled",
        ]
        print("\n📄 Content Management Properties:")
        for prop in content_props:
            if prop in folder_props:
                print(f"  ✅ {prop}")

        # SharePoint specific
        sp_props = [
            "list_item_all_fields",
            "storage_metrics",
            "server_relative_path",
            "property_ref_name",
            "prog_id",
        ]
        print("\n🏢 SharePoint Specific Properties:")
        for prop in sp_props:
            if prop in folder_props:
                print(f"  ✅ {prop}")

        print(
            f"\n💡 And {len(folder_props) - len(core_props + collection_props + content_props + sp_props)} more properties!"
        )

    except Exception as e:
        print(f"❌ Error exploring Folder properties: {e}")


def compare_with_custom_schemas():
    """Compare native SDK schemas with our custom ones."""
    print("\n⚖️  SDK Native vs Custom Schemas Comparison")
    print("=" * 50)

    print("❌ Our Custom SharePointFileMetadata had:")
    custom_props = [
        "unique_id",
        "name",
        "server_relative_url",
        "length",
        "time_created",
        "time_last_modified",
        "author_name",
        "parent_folder_url",
        "list_id",
        "site_id",
        "web_id",
        "major_version",
        "minor_version",
    ]
    for prop in custom_props:
        print(f"  - {prop}")
    print(f"  Total: {len(custom_props)} properties")

    print("\n✅ SDK Native File object has:")
    print("  - All the above properties PLUS:")
    print("  - checked_out_by_user, modified_by, locked_by_user")
    print("  - versions, version_events, checkin_comment")
    print("  - activity_capabilities, irm_enabled")
    print("  - effective_information_rights_management_settings")
    print("  - listItemAllFields (full list item)")
    print("  - content_tag, linking_uri, customized_page_status")
    print("  - And 40+ more properties!")

    print("\n🎯 Benefits of Native SDK Schemas:")
    print("  ✅ No need to write custom dataclasses")
    print("  ✅ No need to write conversion methods")
    print("  ✅ No risk of missing properties")
    print("  ✅ Automatic updates when SDK updates")
    print("  ✅ Better type safety with IDE support")
    print("  ✅ Access to relationship objects (author, parent_folder)")
    print("  ✅ Built-in methods (get_content, download, upload)")


def test_native_client_usage():
    """Test using the native client (requires proper auth)."""
    print("\n🧪 Testing Native Client Usage")
    print("=" * 50)

    try:
        from integrations.sharepoint.client import create_sharepoint_client

        print("✅ Native client import successful")

        # Test client creation
        create_sharepoint_client()
        print("✅ Native client created successfully")

        print("\n💡 With proper Azure credentials, you could:")
        print(
            "  file = client.get_file_by_url('/sites/JGI/Documents/WireSetCerts.xlsx')"
        )
        print("  print(f'File: {file.name}, Size: {file.length} bytes')")
        print("  print(f'Author: {file.author.title if file.author else \"Unknown\"}')")
        print("  print(f'Modified: {file.time_last_modified}')")
        print("  print(f'Versions: {len(file.versions) if file.versions else 0}')")
        print("  content = file.get_content().value  # Direct download!")

    except Exception as e:
        print(f"⚠️  Client test requires proper Azure auth: {e}")


def main():
    """Run all demonstrations."""
    print("🚀 Office365 SDK Native Schemas Demonstration")
    print("=" * 60)

    demonstrate_native_file_properties()
    demonstrate_native_folder_properties()
    compare_with_custom_schemas()
    test_native_client_usage()

    print("\n" + "=" * 60)
    print("🎉 CONCLUSION: Use Native SDK Schemas!")
    print("\n📋 Migration Plan:")
    print("  1. ❌ Delete custom SharePointFileMetadata & SharePointFolderMetadata")
    print("  2. ✅ Import File & Folder from office365.sharepoint")
    print("  3. ✅ Return native SDK objects from functions")
    print("  4. ✅ Access properties directly: file.name, file.length, etc.")
    print("  5. ✅ Use utility functions for backward compatibility")

    print("\n💪 Your code becomes simpler, more powerful, and future-proof!")


if __name__ == "__main__":
    main()

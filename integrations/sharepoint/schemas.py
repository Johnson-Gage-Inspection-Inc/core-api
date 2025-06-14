# integrations/sharepoint/schemas.py
"""
Rich SharePoint schemas using Office365-REST-Python-Client SDK.

This module demonstrates the comprehensive schemas available through the
Office365 SDK, providing much richer type safety and metadata compared
to our current Graph API approach.
"""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from marshmallow import EXCLUDE, Schema, fields, pre_load
from office365.sharepoint.files.file import File
from office365.sharepoint.folders.folder import Folder
from office365.sharepoint.listitems.listitem import ListItem
from office365.sharepoint.principal.users.user import User


class FileCheckOutType(Enum):
    """File checkout types available in SharePoint."""

    NONE = 0
    OFFLINE = 1
    ONLINE = 2


class FileLevel(Enum):
    """SharePoint file level (Draft/Published)."""

    DRAFT = "Draft"
    PUBLISHED = "Published"


@dataclass
class SharePointUserInfo:
    """Rich user information from SharePoint."""

    id: Optional[int] = None
    login_name: Optional[str] = None
    title: Optional[str] = None
    email: Optional[str] = None

    @classmethod
    def from_user_object(
        cls, user_obj: Optional[User]
    ) -> Optional["SharePointUserInfo"]:
        """Create from Office365 User object."""
        if not user_obj:
            return None

        return cls(
            id=getattr(user_obj, "id", None),
            login_name=getattr(user_obj, "login_name", None),
            title=getattr(user_obj, "title", None),
            email=getattr(user_obj, "email", None),
        )


@dataclass
class SharePointFileVersion:
    """File version information."""

    version_id: Optional[int] = None
    version_label: Optional[str] = None
    created: Optional[datetime] = None
    created_by: Optional[SharePointUserInfo] = None
    size: Optional[int] = None
    url: Optional[str] = None


@dataclass
class SharePointFileProperties:
    """
    Comprehensive file properties available through Office365 SDK.

    This demonstrates the rich metadata we get compared to Graph API's
    limited response structure.
    """

    # Core identification
    unique_id: str
    name: str
    title: Optional[str] = None
    server_relative_url: str = ""

    # Content properties
    length: int = 0
    content_tag: Optional[str] = None
    etag: Optional[str] = None

    # Timestamps (Office365 SDK provides proper datetime objects)
    time_created: Optional[datetime] = None
    time_last_modified: Optional[datetime] = None

    # User relationships (rich user objects vs just IDs)
    author: Optional[SharePointUserInfo] = None
    modified_by: Optional[SharePointUserInfo] = None
    checked_out_by: Optional[SharePointUserInfo] = None
    locked_by: Optional[SharePointUserInfo] = None

    # Version control (rich version management)
    major_version: Optional[int] = None
    minor_version: Optional[int] = None
    check_out_type: Optional[FileCheckOutType] = None
    checkin_comment: Optional[str] = None

    # SharePoint metadata
    list_id: Optional[str] = None
    site_id: Optional[str] = None
    web_id: Optional[str] = None
    level: Optional[FileLevel] = None

    # Security & permissions
    irm_enabled: Optional[bool] = None
    has_unique_permissions: Optional[bool] = None

    # File status
    exists: bool = True
    is_checked_out: Optional[bool] = None

    # Parent relationships
    parent_folder_path: Optional[str] = None

    # Custom properties (SharePoint allows custom metadata)
    custom_properties: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_file_object(cls, file_obj: File) -> "SharePointFileProperties":
        """
        Create comprehensive file properties from Office365 File object.

        This shows how the SDK gives us much richer data than Graph API.
        """
        return cls(
            # Core properties
            unique_id=file_obj.unique_id or "",
            name=file_obj.name or "",
            title=getattr(file_obj, "title", None),
            server_relative_url=file_obj.serverRelativeUrl or "",
            # Content
            length=file_obj.length or 0,
            content_tag=file_obj.content_tag,
            # Timestamps - SDK provides proper datetime objects
            time_created=file_obj.time_created,
            time_last_modified=file_obj.time_last_modified,
            # Users - convert to our schema
            author=SharePointUserInfo.from_user_object(file_obj.author),
            modified_by=SharePointUserInfo.from_user_object(file_obj.modified_by),
            checked_out_by=SharePointUserInfo.from_user_object(
                file_obj.checked_out_by_user
            ),
            locked_by=SharePointUserInfo.from_user_object(file_obj.locked_by_user),
            # Versions
            major_version=file_obj.major_version,
            minor_version=file_obj.minor_version,
            check_out_type=(
                FileCheckOutType(file_obj.check_out_type)
                if file_obj.check_out_type
                else None
            ),
            checkin_comment=file_obj.checkin_comment,
            # SharePoint IDs
            list_id=file_obj.list_id,
            site_id=file_obj.site_id,
            web_id=file_obj.web_id,
            level=FileLevel(file_obj.level) if file_obj.level else None,
            # Security
            irm_enabled=file_obj.irm_enabled,
            # Status
            exists=file_obj.exists or False,
            # Parent
            parent_folder_path=(
                file_obj.parent_folder.serverRelativeUrl
                if file_obj.parent_folder
                else None
            ),
        )


@dataclass
class SharePointFolderProperties:
    """
    Rich folder properties from Office365 SDK.
    """

    unique_id: str
    name: str
    server_relative_url: str = ""

    # Timestamps
    time_created: Optional[datetime] = None
    time_last_modified: Optional[datetime] = None

    # Content
    item_count: Optional[int] = None
    folder_count: Optional[int] = None
    file_count: Optional[int] = None

    # SharePoint metadata
    list_id: Optional[str] = None
    site_id: Optional[str] = None
    web_id: Optional[str] = None

    # Status
    exists: bool = True

    @classmethod
    def from_folder_object(cls, folder_obj: Folder) -> "SharePointFolderProperties":
        """Create from Office365 Folder object."""
        return cls(
            unique_id=folder_obj.unique_id or "",
            name=folder_obj.name or "",
            server_relative_url=folder_obj.serverRelativeUrl or "",
            time_created=folder_obj.time_created,
            time_last_modified=folder_obj.time_last_modified,
            item_count=folder_obj.item_count,
            exists=folder_obj.exists or False,
        )


@dataclass
class SharePointListItemProperties:
    """
    Rich list item properties (files are also list items).

    This gives us access to SharePoint's custom columns and metadata
    that aren't available through Graph API.
    """

    id: Optional[int] = None
    title: Optional[str] = None

    # Standard list item fields
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
    author: Optional[SharePointUserInfo] = None
    editor: Optional[SharePointUserInfo] = None

    # File-specific when list item represents a file
    file_ref: Optional[str] = None  # File URL
    file_leaf_ref: Optional[str] = None  # Filename
    file_size_display: Optional[str] = None

    # Custom fields (this is where SharePoint's power shows)
    # These would be populated based on your content types
    custom_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_listitem_object(cls, item_obj: ListItem) -> "SharePointListItemProperties":
        """Create from Office365 ListItem object."""
        # Extract custom fields from the list item
        custom_fields = {}
        if hasattr(item_obj, "properties") and item_obj.properties:
            for key, value in item_obj.properties.items():
                if key not in [
                    "Id",
                    "Title",
                    "Created",
                    "Modified",
                    "Author",
                    "Editor",
                ]:
                    custom_fields[key] = value

        return cls(
            id=getattr(item_obj, "id", None),
            title=getattr(item_obj, "title", None),
            created=getattr(item_obj, "created", None),
            modified=getattr(item_obj, "modified", None),
            author=SharePointUserInfo.from_user_object(
                getattr(item_obj, "author", None)
            ),
            editor=SharePointUserInfo.from_user_object(
                getattr(item_obj, "editor", None)
            ),
            custom_fields=custom_fields,
        )


@dataclass
class SharePointSearchResult:
    """
    Rich search results combining file properties with search metadata.
    """

    file_properties: SharePointFileProperties
    search_score: Optional[float] = None
    hit_highlighted_summary: Optional[str] = None


@dataclass
class SharePointBatchResult:
    """
    Results from batch operations (Office365 SDK supports batching).
    """

    successful_operations: List[Dict[str, Any]] = field(default_factory=list)
    failed_operations: List[Dict[str, Any]] = field(default_factory=list)
    total_operations: int = 0

    @property
    def success_rate(self) -> float:
        """Calculate success rate of batch operation."""
        if self.total_operations == 0:
            return 0.0
        return len(self.successful_operations) / self.total_operations


# SharePoint Integration Schemas
@dataclass
class File:
    """
    Dataclass representing SharePoint file metadata.
    This is the actual data structure used throughout the application.
    """

    id: str
    name: str
    webUrl: str
    size: int
    lastModifiedDateTime: str
    downloadUrl: str
    mimeType: str
    driveId: str
    path: str


class SharePointFileInfoSchema(Schema):
    """Schema for SharePoint file metadata from the Graph API."""

    class Meta:
        unknown = EXCLUDE  # Ignore extra fields not defined below

    # Top-level fields
    id = fields.String(required=True)
    name = fields.String(required=True)
    webUrl = fields.String(required=True)
    size = fields.Integer(required=True)
    lastModifiedDateTime = fields.String(required=True)
    downloadUrl = fields.String(required=True, data_key="@microsoft.graph.downloadUrl")

    # Flattened from nested objects via @pre_load
    mimeType = fields.String(required=True)
    driveId = fields.String(required=True)
    path = fields.String(required=True)

    @pre_load
    def flatten_nested_fields(
        self, data: Dict[str, Any], **kwargs: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Extract nested fields from `file` and `parentReference`."""
        data["mimeType"] = data.get("file", {}).get("mimeType")
        parent = data.get("parentReference", {})
        data["driveId"] = parent.get("driveId")
        data["path"] = parent.get("path")
        return data


class SharePointFileSearchQuerySchema(Schema):
    """Schema for SharePoint file search requests."""

    query = fields.String(
        required=True,
        metadata={"description": "Search query for finding files in SharePoint"},
    )


class SharePointFolderContentsQuerySchema(Schema):
    """Schema for SharePoint folder listing requests."""

    folderPath = fields.String(
        required=False,
        load_default="",
        metadata={"description": "Path to folder within the drive (empty for root)"},
    )

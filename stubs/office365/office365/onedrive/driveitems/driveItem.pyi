from _typeshed import Incomplete
from datetime import datetime
from office365.delta_path import DeltaPath as DeltaPath
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.analytics.item_activity_stat import (
    ItemActivityStat as ItemActivityStat,
)
from office365.onedrive.analytics.item_analytics import ItemAnalytics as ItemAnalytics
from office365.onedrive.base_item import BaseItem as BaseItem
from office365.onedrive.driveitems.audio import Audio as Audio
from office365.onedrive.driveitems.conflict_behavior import (
    ConflictBehavior as ConflictBehavior,
)
from office365.onedrive.driveitems.geo_coordinates import (
    GeoCoordinates as GeoCoordinates,
)
from office365.onedrive.driveitems.image import Image as Image
from office365.onedrive.driveitems.item_preview_info import (
    ItemPreviewInfo as ItemPreviewInfo,
)
from office365.onedrive.driveitems.photo import Photo as Photo
from office365.onedrive.driveitems.publication_facet import (
    PublicationFacet as PublicationFacet,
)
from office365.onedrive.driveitems.remote_item import RemoteItem as RemoteItem
from office365.onedrive.driveitems.retention_label import (
    ItemRetentionLabel as ItemRetentionLabel,
)
from office365.onedrive.driveitems.special_folder import SpecialFolder as SpecialFolder
from office365.onedrive.driveitems.thumbnail_set import ThumbnailSet as ThumbnailSet
from office365.onedrive.driveitems.uploadable_properties import (
    DriveItemUploadableProperties as DriveItemUploadableProperties,
)
from office365.onedrive.drives.recipient import DriveRecipient as DriveRecipient
from office365.onedrive.files.file import File as File
from office365.onedrive.files.system_info import FileSystemInfo as FileSystemInfo
from office365.onedrive.folders.folder import Folder as Folder
from office365.onedrive.internal.paths.children import ChildrenPath as ChildrenPath
from office365.onedrive.internal.paths.url import UrlPath as UrlPath
from office365.onedrive.listitems.item_reference import ItemReference as ItemReference
from office365.onedrive.listitems.list_item import ListItem as ListItem
from office365.onedrive.operations.pending import PendingOperations as PendingOperations
from office365.onedrive.permissions.collection import (
    PermissionCollection as PermissionCollection,
)
from office365.onedrive.permissions.permission import Permission as Permission
from office365.onedrive.sensitivitylabels.extract_result import (
    ExtractSensitivityLabelsResult as ExtractSensitivityLabelsResult,
)
from office365.onedrive.shares.shared import Shared as Shared
from office365.onedrive.versions.drive_item import DriveItemVersion as DriveItemVersion
from office365.onedrive.workbooks.workbook import Workbook as Workbook
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.odata.v4.upload_session import UploadSession as UploadSession
from office365.runtime.odata.v4.upload_session_request import (
    UploadSessionRequest as UploadSessionRequest,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.queries.upload_session import (
    UploadSessionQuery as UploadSessionQuery,
)
from office365.subscriptions.collection import (
    SubscriptionCollection as SubscriptionCollection,
)
from typing import AnyStr, Callable, IO, TypeVar
from typing_extensions import Self

P_T = TypeVar("P_T")

class DriveItem(BaseItem):
    def get_files(
        self, recursive: bool = False, page_size: int | None = None
    ) -> EntityCollection["DriveItem"]: ...
    def get_folders(
        self, recursive: bool = False, page_size: int | None = None
    ) -> EntityCollection["DriveItem"]: ...
    def get_by_path(self, url_path: str) -> DriveItem: ...
    def create_powerpoint(self, name: str) -> DriveItem: ...
    def create_link(
        self,
        link_type: str,
        scope: str | None = None,
        expiration_datetime: datetime | None = None,
        password: str | None = None,
        message: str | None = None,
        retain_inherited_permissions: bool | None = None,
    ) -> Permission: ...
    def discard_checkout(self): ...
    def extract_sensitivity_labels(
        self,
    ) -> ClientResult[ExtractSensitivityLabelsResult]: ...
    def follow(self) -> Self: ...
    def unfollow(self) -> Self: ...
    def checkout(self) -> Self: ...
    def checkin(self, comment: str, checkin_as: str | None = None) -> Self: ...
    def resumable_upload(
        self,
        source_path: str,
        chunk_size: int = 2000000,
        chunk_uploaded: Callable[[int], None] | None = None,
    ) -> DriveItem: ...
    def create_upload_session(
        self, item: DriveItemUploadableProperties
    ) -> ClientResult[UploadSession]: ...
    def upload(self, name, content): ...
    def upload_file(self, path_or_file: str | IO) -> DriveItem: ...
    def upload_folder(
        self, path: str, file_uploaded: Callable[[DriveItem], None] = None
    ) -> DriveItem: ...
    def get_content(self, format_name: str | None = None) -> ClientResult[AnyStr]: ...
    def download(self, file_object: IO) -> Self: ...
    def download_folder(
        self,
        download_file: IO,
        after_file_downloaded: Callable[[DriveItem], None] = None,
        recursive: bool = True,
    ) -> DriveItem: ...
    def download_session(
        self,
        file_object: IO,
        chunk_downloaded: None = None,
        chunk_size: int | None = ...,
    ) -> Self: ...
    def create_folder(
        self, name: str, conflict_behavior: ConflictBehavior | None = ...
    ) -> DriveItem: ...
    def convert(self, format_name: str) -> ClientResult[AnyStr]: ...
    def copy(
        self,
        name: str = None,
        parent: ItemReference | DriveItem = None,
        conflict_behavior: str = ...,
    ) -> ClientResult[str]: ...
    def move(
        self,
        name: str = None,
        parent: ItemReference | DriveItem = None,
        conflict_behavior: str = ...,
    ) -> DriveItem: ...
    def rename(self, new_name: str) -> DriveItem: ...
    def search(self, query_text: str) -> EntityCollection["DriveItem"]: ...
    def invite(
        self,
        recipients: list[str],
        message: str,
        require_sign_in: bool | None = True,
        send_invitation: bool | None = True,
        roles: list[str] | None = None,
        expiration_datetime: datetime | None = None,
        password: str | None = None,
        retain_inherited_permissions: bool | None = None,
    ) -> PermissionCollection: ...
    def get_activities_by_interval(
        self,
        start_dt: Incomplete | None = None,
        end_dt: Incomplete | None = None,
        interval: Incomplete | None = None,
    ): ...
    def permanent_delete(self): ...
    def restore(
        self, parent_reference: ItemReference | None = None, name: str = None
    ) -> DriveItem: ...
    def preview(
        self, page: None, zoom: None = None
    ) -> ClientResult[ItemPreviewInfo]: ...
    def validate_permission(
        self, challenge_token: str | None = None, password: str | None = None
    ) -> Self: ...
    @property
    def audio(self) -> Audio: ...
    @property
    def image(self) -> Image: ...
    @property
    def photo(self) -> Photo: ...
    @property
    def location(self) -> GeoCoordinates: ...
    @property
    def file_system_info(self) -> FileSystemInfo: ...
    @property
    def folder(self) -> Folder: ...
    @property
    def file(self) -> File: ...
    @property
    def is_folder(self) -> bool: ...
    @property
    def is_file(self) -> bool: ...
    @property
    def shared(self) -> Shared: ...
    @property
    def web_dav_url(self) -> None: ...
    @property
    def children(self) -> EntityCollection["DriveItem"]: ...
    @property
    def listItem(self) -> ListItem: ...
    @property
    def workbook(self) -> Workbook: ...
    @property
    def pending_operations(self) -> PendingOperations: ...
    @property
    def permissions(self) -> PermissionCollection: ...
    @property
    def retention_label(self) -> ItemRetentionLabel: ...
    @property
    def publication(self) -> PublicationFacet: ...
    @property
    def remote_item(self) -> RemoteItem: ...
    @property
    def special_folder(self) -> SpecialFolder: ...
    @property
    def versions(self) -> EntityCollection[DriveItemVersion]: ...
    @property
    def thumbnails(self) -> EntityCollection[ThumbnailSet]: ...
    @property
    def analytics(self) -> ItemAnalytics: ...
    @property
    def delta(self) -> EntityCollection[DriveItem]: ...
    @property
    def subscriptions(self) -> SubscriptionCollection: ...
    def set_property(self, name, value, persist_changes: bool = True): ...
    def get_property(self, name: str, default_value: P_T = None) -> P_T: ...

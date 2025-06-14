import datetime

from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.paths.v3.entity import EntityPath as EntityPath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.attachments.collection import (
    AttachmentCollection as AttachmentCollection,
)
from office365.sharepoint.changes.collection import ChangeCollection as ChangeCollection
from office365.sharepoint.changes.query import ChangeQuery as ChangeQuery
from office365.sharepoint.comments.collection import (
    CommentCollection as CommentCollection,
)
from office365.sharepoint.fields.image_value import ImageFieldValue as ImageFieldValue
from office365.sharepoint.fields.lookup_value import (
    FieldLookupValue as FieldLookupValue,
)
from office365.sharepoint.fields.multi_lookup_value import (
    FieldMultiLookupValue as FieldMultiLookupValue,
)
from office365.sharepoint.fields.string_values import (
    FieldStringValues as FieldStringValues,
)
from office365.sharepoint.fields.url_value import FieldUrlValue as FieldUrlValue
from office365.sharepoint.likes.liked_by_information import (
    LikedByInformation as LikedByInformation,
)
from office365.sharepoint.listitems.compliance_info import (
    ListItemComplianceInfo as ListItemComplianceInfo,
)
from office365.sharepoint.listitems.form_update_value import (
    ListItemFormUpdateValue as ListItemFormUpdateValue,
)
from office365.sharepoint.listitems.update_parameters import (
    ListItemUpdateParameters as ListItemUpdateParameters,
)
from office365.sharepoint.listitems.versions.collection import (
    ListItemVersionCollection as ListItemVersionCollection,
)
from office365.sharepoint.permissions.securable_object import (
    SecurableObject as SecurableObject,
)
from office365.sharepoint.policy.dlp_policy_tip import DlpPolicyTip as DlpPolicyTip
from office365.sharepoint.reputationmodel.reputation import Reputation as Reputation
from office365.sharepoint.sharing.external_site_option import (
    ExternalSharingSiteOption as ExternalSharingSiteOption,
)
from office365.sharepoint.sharing.links.share_request import (
    ShareLinkRequest as ShareLinkRequest,
)
from office365.sharepoint.sharing.links.share_response import (
    ShareLinkResponse as ShareLinkResponse,
)
from office365.sharepoint.sharing.links.share_settings import (
    ShareLinkSettings as ShareLinkSettings,
)
from office365.sharepoint.sharing.object_sharing_information import (
    ObjectSharingInformation as ObjectSharingInformation,
)
from office365.sharepoint.sharing.result import SharingResult as SharingResult
from office365.sharepoint.taxonomy.field_value import (
    TaxonomyFieldValueCollection as TaxonomyFieldValueCollection,
)
from office365.sharepoint.ui.applicationpages.peoplepicker.web_service_interface import (
    ClientPeoplePickerWebServiceInterface as ClientPeoplePickerWebServiceInterface,
)

class ListItem(SecurableObject):
    def __init__(
        self,
        context,
        resource_path: Incomplete | None = None,
        parent_list: Incomplete | None = None,
    ) -> None: ...
    def archive(self): ...
    def share_link(
        self,
        link_kind: int,
        expiration: datetime.datetime | None = None,
        role: int | None = None,
        password: str | None = None,
    ) -> ClientResult[ShareLinkResponse]: ...
    def unshare_link(self, link_kind, share_id: Incomplete | None = None): ...
    def delete_link_by_kind(self, link_kind): ...
    def set_rating(self, value): ...
    def set_like(self, value): ...
    def get_wopi_frame_url(self, action): ...
    def recycle(self): ...
    def get_changes(self, query: Incomplete | None = None): ...
    def share(
        self,
        user_principal_name,
        share_option=...,
        send_email: bool = True,
        email_subject: Incomplete | None = None,
        email_body: Incomplete | None = None,
    ): ...
    def unshare(self): ...
    def get_sharing_information(self): ...
    def validate_update_list_item(
        self,
        form_values,
        new_document_update: bool = False,
        checkin_comment: Incomplete | None = None,
        dates_in_utc: Incomplete | None = None,
    ): ...
    def update(self): ...
    def update_ex(
        self,
        bypass_quota_check: Incomplete | None = None,
        bypass_shared_lock: Incomplete | None = None,
    ): ...
    def system_update(self): ...
    def update_overwrite_version(self): ...
    def set_comments_disabled(self, value): ...
    def set_compliance_tag_with_hold(self, compliance_tag): ...
    def get_comments(self): ...
    def override_policy_tip(self, user_action, justification): ...
    def parse_and_set_field_value(self, field_name, value): ...
    @property
    def display_name(self) -> str | None: ...
    @property
    def parent_list(self): ...
    @property
    def file(self): ...
    @property
    def folder(self): ...
    @property
    def attachment_files(self) -> AttachmentCollection: ...
    @property
    def content_type(self): ...
    @property
    def effective_base_permissions(self): ...
    @property
    def effective_base_permissions_for_ui(self): ...
    @property
    def field_values(self) -> dict | None: ...
    @property
    def comments_disabled(self) -> bool | None: ...
    @property
    def file_system_object_type(self) -> str | None: ...
    @property
    def icon_overlay(self) -> str | None: ...
    @property
    def id(self) -> int | None: ...
    @property
    def server_redirected_embed_uri(self) -> str | None: ...
    @property
    def server_redirected_embed_url(self) -> str | None: ...
    @property
    def client_title(self) -> str | None: ...
    @property
    def compliance_info(self): ...
    @property
    def comments_disabled_scope(self) -> str | None: ...
    @property
    def get_dlp_policy_tip(self): ...
    @property
    def field_values_as_html(self): ...
    @property
    def liked_by_information(self): ...
    @property
    def versions(self): ...
    @property
    def doc_id(self) -> str | None: ...
    @property
    def doc_id_url(self) -> FieldUrlValue | None: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
    def set_property(self, name, value, persist_changes: bool = True): ...
    def ensure_type_name(self, target_list, action: Incomplete | None = None): ...

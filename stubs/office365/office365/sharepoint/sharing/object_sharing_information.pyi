from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.sharing.links.info import SharingLinkInfo as SharingLinkInfo
from office365.sharepoint.sharing.object_sharing_information_user import (
    ObjectSharingInformationUser as ObjectSharingInformationUser,
)

class ObjectSharingInformation(Entity):
    @staticmethod
    def can_current_user_share(context, doc_id): ...
    @staticmethod
    def can_current_user_share_remote(context, doc_id): ...
    @staticmethod
    def get_web_sharing_information(
        context,
        exclude_current_user: Incomplete | None = None,
        exclude_site_admin: Incomplete | None = None,
        exclude_security_groups: Incomplete | None = None,
        retrieve_anonymous_links: Incomplete | None = None,
        retrieve_user_info_details: Incomplete | None = None,
        check_for_access_requests: Incomplete | None = None,
    ): ...
    def get_shared_with_users(self): ...
    @staticmethod
    def get_list_item_sharing_information(
        context: ClientContext,
        list_id: str,
        item_id: int,
        exclude_current_user: bool | None = True,
        exclude_site_admin: bool | None = True,
        exclude_security_groups: bool | None = True,
        retrieve_anonymous_links: bool | None = False,
        retrieve_user_info_details: bool | None = False,
        check_for_access_requests: bool | None = False,
        return_type: ObjectSharingInformation | None = None,
    ) -> ObjectSharingInformation: ...
    @property
    def anonymous_edit_link(self) -> str | None: ...
    @property
    def anonymous_view_link(self) -> str | None: ...
    @property
    def can_be_shared(self) -> bool | None: ...
    @property
    def can_be_unshared(self) -> bool | None: ...
    @property
    def can_manage_permissions(self) -> bool | None: ...
    @property
    def has_pending_access_requests(self) -> bool | None: ...
    @property
    def has_permission_levels(self) -> bool | None: ...
    @property
    def sharing_links(self) -> ClientValueCollection[SharingLinkInfo]: ...
    @property
    def shared_with_users_collection(
        self,
    ) -> EntityCollection[ObjectSharingInformationUser]: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...
    def set_property(self, name, value, persist_changes: bool = True): ...

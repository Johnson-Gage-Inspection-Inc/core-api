from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.permissions.roles.definitions.definition import RoleDefinition as RoleDefinition
from office365.sharepoint.portal.userprofiles.sharedwithme.view_item_removal_result import SharedWithMeViewItemRemovalResult as SharedWithMeViewItemRemovalResult
from office365.sharepoint.sharing.user_role_assignment import UserRoleAssignment as UserRoleAssignment
from office365.sharepoint.sharing.user_sharing_result import UserSharingResult as UserSharingResult

class DocumentSharingManager(Entity):
    @staticmethod
    def get_role_definition(context, role): ...
    @staticmethod
    def remove_items_from_shared_with_me_view(context, item_urls): ...
    @staticmethod
    def update_document_sharing_info(context, resource_address, user_role_assignments, validate_existing_permissions: Incomplete | None = None, additive_mode: Incomplete | None = None, send_server_managed_notification: Incomplete | None = None, custom_message: Incomplete | None = None, include_anonymous_links_in_notification: Incomplete | None = None, propagate_acl: Incomplete | None = None, return_type: Incomplete | None = None): ...
    @property
    def entity_type_name(self): ...

from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.compliance.tag import ComplianceTag as ComplianceTag
from office365.sharepoint.entity import Entity as Entity

class SPPolicyStoreProxy(Entity):
    @staticmethod
    def check_site_is_deletable_by_id(
        context: ClientContext,
        site_id: str,
        return_type: ClientResult[bool] | None = None,
    ) -> ClientResult[bool]: ...
    @staticmethod
    def is_site_deletable(
        context: ClientContext,
        site_url: str,
        return_type: ClientResult[bool] | None = None,
    ) -> ClientResult[bool]: ...
    @staticmethod
    def get_available_tags_for_site(
        context, site_url, return_type: Incomplete | None = None
    ): ...
    def get_dynamic_scope_binding_by_site_id(self, site_id): ...
    @staticmethod
    def get_list_compliance_tag(
        context, list_url, return_type: Incomplete | None = None
    ): ...
    @staticmethod
    def set_list_compliance_tag(
        context,
        list_url,
        compliance_tag_value,
        block_delete: Incomplete | None = None,
        block_edit: Incomplete | None = None,
        sync_to_items: Incomplete | None = None,
    ): ...
    @staticmethod
    def lock_record_item(
        context,
        list_url,
        item_id,
        refresh_labeled_time,
        return_type: Incomplete | None = None,
    ): ...
    @property
    def entity_type_name(self): ...

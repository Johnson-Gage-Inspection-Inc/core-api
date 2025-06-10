from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.files.file import File as File
from office365.sharepoint.utilities.principal_info import PrincipalInfo as PrincipalInfo

class Utility(Entity):
    def __init__(self, context) -> None: ...
    @staticmethod
    def create_email_body_for_invitation(context, page_address): ...
    @staticmethod
    def get_current_user_email_addresses(context): ...
    @staticmethod
    def get_user_permission_levels(context): ...
    @staticmethod
    def search_principals_using_context_web(
        context,
        s_input,
        sources,
        scopes,
        max_count,
        group_name: Incomplete | None = None,
    ): ...
    @staticmethod
    def create_wiki_page_in_context_web(
        context, parameters, return_type: Incomplete | None = None
    ): ...
    @staticmethod
    def send_email(context, properties): ...
    @staticmethod
    def unmark_discussion_as_featured(context, list_id, topic_ids): ...
    @staticmethod
    def expand_groups_to_principals(
        context,
        inputs,
        max_count: Incomplete | None = None,
        return_type: Incomplete | None = None,
    ): ...
    @staticmethod
    def log_custom_app_error(
        context: ClientContext, error: str
    ) -> ClientResult[int]: ...
    @staticmethod
    def resolve_principal_in_current_context(
        context,
        string_input,
        scopes: Incomplete | None = None,
        sources: Incomplete | None = None,
        input_is_email_only: Incomplete | None = None,
        add_to_user_info_list: Incomplete | None = None,
        match_user_info_list: Incomplete | None = None,
    ): ...
    @property
    def entity_type_name(self): ...

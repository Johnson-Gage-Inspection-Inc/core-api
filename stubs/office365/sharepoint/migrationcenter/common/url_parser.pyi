from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.entity import Entity as Entity

class MigrationUrlParser(Entity):
    def __init__(self, context: ClientContext, user_input_destination_url: str, retrive_all_lists: bool, retrieve_all_lists_sub_folders: bool, force_my_site_default_list: bool, migration_type: str, current_context_site_subscription_id: str) -> None: ...
    @property
    def entity_type_name(self): ...

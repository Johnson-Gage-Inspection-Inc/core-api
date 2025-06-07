from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sites.language_collection import LanguageCollection as LanguageCollection

class ServerSettings(Entity):
    def __init__(self, context) -> None: ...
    @staticmethod
    def is_sharepoint_online(context): ...
    @staticmethod
    def get_blocked_file_extensions(context): ...
    @staticmethod
    def get_global_installed_languages(context, compatibility_level): ...

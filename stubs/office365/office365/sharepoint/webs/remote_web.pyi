from office365.onedrive.lists.list import List as List
from office365.runtime.client_object import ClientObject as ClientObject
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.webs.web import Web as Web

class RemoteWeb(ClientObject):
    def get_list_by_server_relative_url(self, server_relative_url): ...
    @staticmethod
    def create(context, request_url): ...
    @property
    def web(self): ...

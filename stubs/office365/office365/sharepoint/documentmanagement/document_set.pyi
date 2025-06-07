from office365.runtime.http.http_method import HttpMethod as HttpMethod
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.queries.client_query import ClientQuery as ClientQuery
from office365.sharepoint.folders.folder import Folder as Folder
from office365.sharepoint.lists.list import List as List

class DocumentSet(Folder):
    @staticmethod
    def create(context, parent_folder, name, ct_id: str = "0x0120D520"): ...
    @staticmethod
    def get_document_set(context, folder): ...

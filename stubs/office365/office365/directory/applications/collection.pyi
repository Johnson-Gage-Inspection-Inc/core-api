from _typeshed import Incomplete
from office365.delta_collection import DeltaCollection as DeltaCollection
from office365.directory.applications.application import Application as Application
from office365.runtime.paths.appid import AppIdPath as AppIdPath

class ApplicationCollection(DeltaCollection[Application]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def add(self, display_name, **kwargs): ...
    def get_by_app_id(self, app_id: str) -> Application: ...

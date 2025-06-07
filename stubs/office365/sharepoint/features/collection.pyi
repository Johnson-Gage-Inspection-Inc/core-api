from _typeshed import Incomplete
from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.features.feature import Feature as Feature

class FeatureCollection(EntityCollection[Feature]):
    def __init__(self, context, resource_path: Incomplete | None = None, parent: Incomplete | None = None) -> None: ...
    def add(self, feature_id: str, force: bool, featdef_scope: int, verify_if_activated: bool = False) -> Feature: ...
    def get_by_id(self, feature_id: str) -> Feature: ...

from _typeshed import Incomplete
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.features.definitions.definition import FeatureDefinition as FeatureDefinition

class FeatureDefinitionCollection(EntityCollection):
    def __init__(self, context, resource_path: Incomplete | None = None, parent: Incomplete | None = None) -> None: ...
    def get_feature_definition(self, feature_display_name, compatibility_level: Incomplete | None = None): ...

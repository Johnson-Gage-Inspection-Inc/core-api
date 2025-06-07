from _typeshed import Incomplete
from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.eventreceivers.definition import EventReceiverDefinition as EventReceiverDefinition

class EventReceiverDefinitionCollection(EntityCollection[EventReceiverDefinition]):
    def __init__(self, context, resource_path: Incomplete | None = None, parent: Incomplete | None = None) -> None: ...
    def get_by_id(self, event_receiver_id): ...

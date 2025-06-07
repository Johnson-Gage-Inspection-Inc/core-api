from _typeshed import Incomplete
from office365.entity_collection import EntityCollection as EntityCollection
from office365.onedrive.termstore.terms.label import LocalizedLabel as LocalizedLabel
from office365.onedrive.termstore.terms.term import Term as Term
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.queries.create_entity import CreateEntityQuery as CreateEntityQuery

class TermCollection(EntityCollection[Term]):
    def __init__(self, context, resource_path: Incomplete | None = None, parent_set: Incomplete | None = None) -> None: ...
    def add(self, label): ...

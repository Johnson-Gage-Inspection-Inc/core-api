from _typeshed import Incomplete
from office365.sharepoint.taxonomy.groups.group import TermGroup as TermGroup
from office365.sharepoint.taxonomy.item_collection import TaxonomyItemCollection as TaxonomyItemCollection

class TermGroupCollection(TaxonomyItemCollection[TermGroup]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def get_by_name(self, name): ...

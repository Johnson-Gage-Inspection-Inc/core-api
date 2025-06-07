from _typeshed import Incomplete
from office365.sharepoint.taxonomy.item_collection import TaxonomyItemCollection as TaxonomyItemCollection
from office365.sharepoint.taxonomy.sets.set import TermSet as TermSet

class TermSetCollection(TaxonomyItemCollection[TermSet]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...

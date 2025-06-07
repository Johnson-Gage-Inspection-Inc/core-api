from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.taxonomy.item import TaxonomyItem as TaxonomyItem
from office365.sharepoint.taxonomy.item_collection import (
    TaxonomyItemCollection as TaxonomyItemCollection,
)
from office365.sharepoint.taxonomy.sets.collection import (
    TermSetCollection as TermSetCollection,
)
from office365.sharepoint.taxonomy.sets.set import TermSet as TermSet

class TermGroup(TaxonomyItem):
    def get_term_sets_by_name(self, label, lcid: Incomplete | None = None): ...
    @property
    def term_sets(self) -> TaxonomyItemCollection[TermSet]: ...
    @property
    def display_name(self) -> str | None: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...

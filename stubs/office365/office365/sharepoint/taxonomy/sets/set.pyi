from _typeshed import Incomplete
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.taxonomy.item import TaxonomyItem as TaxonomyItem
from office365.sharepoint.taxonomy.item_collection import (
    TaxonomyItemCollection as TaxonomyItemCollection,
)
from office365.sharepoint.taxonomy.sets.name import LocalizedName as LocalizedName
from office365.sharepoint.taxonomy.terms.term import Term as Term

class TermSet(TaxonomyItem):
    @property
    def localized_names(self): ...
    @property
    def terms(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...

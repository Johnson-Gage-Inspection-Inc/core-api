from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.function import FunctionQuery as FunctionQuery
from office365.runtime.types.collections import StringCollection as StringCollection
from office365.sharepoint.taxonomy.groups.collection import TermGroupCollection as TermGroupCollection
from office365.sharepoint.taxonomy.item import TaxonomyItem as TaxonomyItem
from office365.sharepoint.taxonomy.item_collection import TaxonomyItemCollection as TaxonomyItemCollection
from office365.sharepoint.taxonomy.sets.collection import TermSetCollection as TermSetCollection
from office365.sharepoint.taxonomy.terms.term import Term as Term

class TermStore(TaxonomyItem):
    def get_term_sets_by_name(self, label, lcid: int = 1033): ...
    def search_term(self, label, set_id: Incomplete | None = None, parent_term_id: Incomplete | None = None, language_tag: Incomplete | None = None): ...
    @property
    def default_language_tag(self) -> str | None: ...
    @property
    def language_tags(self): ...
    @property
    def term_groups(self) -> TermGroupCollection: ...
    def get_property(self, name, default_value: Incomplete | None = None): ...

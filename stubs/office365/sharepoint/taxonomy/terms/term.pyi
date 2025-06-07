import datetime
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.taxonomy.item import TaxonomyItem as TaxonomyItem
from office365.sharepoint.taxonomy.terms.label import Label as Label

class Term(TaxonomyItem):
    @property
    def is_deprecated(self) -> bool: ...
    @property
    def children_count(self) -> int: ...
    @property
    def created_datetime(self) -> datetime.datetime: ...
    @property
    def labels(self): ...
    @property
    def parent(self): ...

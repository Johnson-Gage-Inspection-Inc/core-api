from _typeshed import Incomplete
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.marketplace.app_metadata_collection import CorporateCatalogAppMetadataCollection as CorporateCatalogAppMetadataCollection

class SiteCollectionCorporateCatalogAccessor(Entity):
    @property
    def available_apps(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...

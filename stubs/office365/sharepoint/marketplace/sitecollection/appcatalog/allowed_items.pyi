from _typeshed import Incomplete
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.marketplace.sitecollection.appcatalog.allowed_item import SiteCollectionAppCatalogAllowedItem as SiteCollectionAppCatalogAllowedItem

class SiteCollectionAppCatalogAllowedItems(EntityCollection[SiteCollectionAppCatalogAllowedItem]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...

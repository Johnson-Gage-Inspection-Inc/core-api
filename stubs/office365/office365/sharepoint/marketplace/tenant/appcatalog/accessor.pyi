from _typeshed import Incomplete
from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.files.file import File as File
from office365.sharepoint.marketplace.app_metadata import (
    CorporateCatalogAppMetadata as CorporateCatalogAppMetadata,
)
from office365.sharepoint.marketplace.app_metadata_collection import (
    CorporateCatalogAppMetadataCollection as CorporateCatalogAppMetadataCollection,
)
from office365.sharepoint.marketplace.corporatecuratedgallery.app_request_information import (
    SPStoreAppRequestInformation as SPStoreAppRequestInformation,
)
from office365.sharepoint.marketplace.corporatecuratedgallery.app_response_information import (
    SPStoreAppResponseInformation as SPStoreAppResponseInformation,
)
from office365.sharepoint.marketplace.corporatecuratedgallery.app_upgrade_availability import (
    AppUpgradeAvailability as AppUpgradeAvailability,
)
from office365.sharepoint.marketplace.corporatecuratedgallery.card_designs import (
    CardDesigns as CardDesigns,
)
from office365.sharepoint.marketplace.corporatecuratedgallery.teams_package_download import (
    TeamsPackageDownload as TeamsPackageDownload,
)
from office365.sharepoint.marketplace.sitecollection.appcatalog.allowed_items import (
    SiteCollectionAppCatalogAllowedItems as SiteCollectionAppCatalogAllowedItems,
)

class TenantCorporateCatalogAccessor(Entity):
    def add(self, content, overwrite, url: Incomplete | None = None): ...
    def app_from_path(self, path: str, overwrite: bool) -> File: ...
    def app_requests(self): ...
    def download_teams_solution(self, _id): ...
    def get_app_by_id(self, item_unique_id): ...
    def is_app_upgrade_available(self, _id): ...
    def upload(self, content, overwrite, url, xor_hash: Incomplete | None = None): ...
    def send_app_request_status_notification_email(self, request_guid): ...
    @property
    def available_apps(self): ...
    @property
    def card_designs(self): ...
    @property
    def site_collection_app_catalogs_sites(self): ...
    @property
    def entity_type_name(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...

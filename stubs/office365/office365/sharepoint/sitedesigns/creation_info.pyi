from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class SiteDesignCreationInfo(ClientValue):
    Id: Incomplete
    Title: Incomplete
    Description: Incomplete
    WebTemplate: Incomplete
    SiteScriptIds: Incomplete
    DesignPackageId: Incomplete
    def __init__(
        self,
        _id: Incomplete | None = None,
        title: Incomplete | None = None,
        description: Incomplete | None = None,
        web_template: Incomplete | None = None,
        site_script_ids: Incomplete | None = None,
        design_package_id: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...

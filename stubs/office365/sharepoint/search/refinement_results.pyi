from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.sharepoint.search.refiner.refiner import Refiner as Refiner

class RefinementResults(ClientValue):
    GroupTemplateId: Incomplete
    ItemTemplateId: Incomplete
    Refiners: Incomplete
    Properties: Incomplete
    ResultTitle: Incomplete
    ResultTitleUrl: Incomplete
    def __init__(self, group_template_id: Incomplete | None = None, item_template_id: Incomplete | None = None, refiners: Incomplete | None = None, properties: Incomplete | None = None, result_title: Incomplete | None = None, result_title_url: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...

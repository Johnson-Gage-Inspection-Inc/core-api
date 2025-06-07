from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class CustomResult(ClientValue):
    GroupTemplateId: Incomplete
    ItemTemplateId: Incomplete
    Properties: Incomplete
    ResultTitle: Incomplete
    def __init__(self, group_template_id: Incomplete | None = None, item_template_id: Incomplete | None = None, result_title: Incomplete | None = None, properties: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...

from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class TaxonomyFieldCreateXmlParameters(ClientValue):
    Name: Incomplete
    SspId: Incomplete
    TermSetId: Incomplete
    AnchorId: Incomplete
    FieldId: Incomplete
    TextFieldId: Incomplete
    WebId: Incomplete
    ListId: Incomplete
    AllowMultipleValues: Incomplete
    def __init__(
        self,
        name,
        term_set_id,
        term_store_id: Incomplete | None = None,
        anchor_id: str = "00000000-0000-0000-0000-000000000000",
        allow_multiple_values: bool = False,
    ) -> None: ...
    @property
    def type_name(self): ...
    @property
    def schema_xml(self): ...

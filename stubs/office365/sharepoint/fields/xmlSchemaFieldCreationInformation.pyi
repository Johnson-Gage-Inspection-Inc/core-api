from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class XmlSchemaFieldCreationInformation(ClientValue):
    SchemaXml: Incomplete
    Options: Incomplete
    def __init__(self, schema_xml: Incomplete | None = None, options: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...

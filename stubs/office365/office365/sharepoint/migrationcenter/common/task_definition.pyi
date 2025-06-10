from office365.runtime.client_value import ClientValue as ClientValue

class MigrationTaskDefinition(ClientValue):
    @property
    def entity_type_name(self) -> str: ...

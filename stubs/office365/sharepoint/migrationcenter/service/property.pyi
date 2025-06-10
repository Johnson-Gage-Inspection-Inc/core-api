from office365.runtime.client_value import ClientValue as ClientValue

class MigrationProperty(ClientValue):
    @property
    def entity_type_name(self): ...

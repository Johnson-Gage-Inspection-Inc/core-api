from office365.runtime.client_value import ClientValue as ClientValue

class Role(ClientValue):
    View: int
    Edit: int
    Owner: int
    @property
    def entity_type_name(self): ...

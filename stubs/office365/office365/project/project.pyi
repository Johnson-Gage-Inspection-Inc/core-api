from office365.runtime.client_object import ClientObject as ClientObject

class Project(ClientObject):
    @property
    def entity_type_name(self): ...

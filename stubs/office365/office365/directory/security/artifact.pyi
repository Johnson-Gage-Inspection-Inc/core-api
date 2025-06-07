from office365.entity import Entity as Entity

class Artifact(Entity):
    @property
    def entity_type_name(self): ...

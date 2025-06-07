from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.outlook.people.profile_card_property import ProfileCardProperty as ProfileCardProperty
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class PeopleAdminSettings(Entity):
    @property
    def profile_card_properties(self): ...

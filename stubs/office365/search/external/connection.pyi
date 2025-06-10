from office365.entity import Entity as Entity
from office365.search.external.configuration import Configuration as Configuration
from office365.search.external.search_settings import SearchSettings as SearchSettings

class ExternalConnection(Entity):
    @property
    def configuration(self): ...
    @property
    def search_settings(self): ...
    @property
    def entity_type_name(self): ...

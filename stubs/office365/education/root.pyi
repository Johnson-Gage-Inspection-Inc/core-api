from office365.education.class_type import EducationClass as EducationClass
from office365.education.user import EducationUser as EducationUser
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class EducationRoot(Entity):
    @property
    def classes(self): ...
    @property
    def me(self): ...
    @property
    def users(self): ...

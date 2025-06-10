from _typeshed import Incomplete
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.viva.community import Community as Community
from office365.teams.viva.learning.courses.activity import (
    LearningCourseActivity as LearningCourseActivity,
)
from office365.teams.viva.learning.provider import LearningProvider as LearningProvider

class EmployeeExperience(Entity):
    @property
    def communities(self): ...
    @property
    def learning_course_activities(self): ...
    @property
    def learning_providers(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...

from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.teams.viva.learning.courses.activity import LearningCourseActivity as LearningCourseActivity

class EmployeeExperienceUser(Entity):
    @property
    def learning_course_activities(self) -> EntityCollection[LearningCourseActivity]: ...

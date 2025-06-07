from _typeshed import Incomplete
from office365.admin.microsoft365_apps import AdminMicrosoft365Apps as AdminMicrosoft365Apps
from office365.admin.people_settings import PeopleAdminSettings as PeopleAdminSettings
from office365.admin.report_settings import AdminReportSettings as AdminReportSettings
from office365.admin.sharepoint import Sharepoint as Sharepoint
from office365.entity import Entity as Entity
from office365.intune.servicecommunications.announcement import ServiceAnnouncement as ServiceAnnouncement
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class Admin(Entity):
    @property
    def microsoft365_apps(self): ...
    @property
    def sharepoint(self): ...
    @property
    def service_announcement(self): ...
    @property
    def report_settings(self): ...
    @property
    def people(self): ...
    def get_property(self, name, default_value: Incomplete | None = None): ...

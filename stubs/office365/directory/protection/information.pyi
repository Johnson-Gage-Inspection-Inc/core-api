from _typeshed import Incomplete
from office365.directory.protection.threatassessment.requests.request import (
    ThreatAssessmentRequest as ThreatAssessmentRequest,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.http.request_options import RequestOptions as RequestOptions
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)

class InformationProtection(Entity):
    def create_email_file_assessment(
        self, recipient_email, content_data, expected_assessment, category
    ): ...
    def create_file_assessment(
        self, file_name, content_data, expected_assessment, category
    ): ...
    def create_url_assessment(self, url, expected_assessment, category): ...
    def create_mail_assessment(
        self,
        message,
        recipient: Incomplete | None = None,
        expected_assessment: str = "block",
        category: str = "spam",
    ): ...
    @property
    def threat_assessment_requests(
        self,
    ) -> EntityCollection[ThreatAssessmentRequest]: ...

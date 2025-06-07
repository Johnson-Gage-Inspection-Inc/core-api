from office365.directory.protection.threatassessment.requests.request import (
    ThreatAssessmentRequest as ThreatAssessmentRequest,
)

class EmailFileAssessmentRequest(ThreatAssessmentRequest):
    @property
    def content_data(self) -> str | None: ...
    @property
    def file_name(self) -> str | None: ...

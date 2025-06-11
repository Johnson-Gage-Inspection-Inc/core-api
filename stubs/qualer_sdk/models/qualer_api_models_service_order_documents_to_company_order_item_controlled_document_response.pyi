from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse(
    BaseModel
):
    service_order_id: StrictInt | None
    service_order_item_id: StrictInt | None
    guid: StrictStr | None
    document_name: StrictStr | None
    file_name: StrictStr | None
    document_type: StrictStr | None
    revision_number: StrictInt | None
    report_type: StrictStr | None
    download_url: StrictStr | None
    def document_type_validate_enum(cls, value): ...
    def report_type_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> (
        QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse
    ): ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> (
        QualerApiModelsServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse
    ): ...

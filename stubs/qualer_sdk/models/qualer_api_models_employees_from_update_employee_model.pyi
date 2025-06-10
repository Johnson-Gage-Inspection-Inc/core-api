from pydantic import BaseModel, StrictStr as StrictStr

class QualerApiModelsEmployeesFromUpdateEmployeeModel(BaseModel):
    first_name: StrictStr | None
    last_name: StrictStr | None
    subscription_email: StrictStr | None
    mobile_phone: StrictStr | None
    office_phone: StrictStr | None
    alias: StrictStr | None
    title: StrictStr | None
    culture_name: StrictStr | None
    culture_ui_name: StrictStr | None
    image_url: StrictStr | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsEmployeesFromUpdateEmployeeModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsEmployeesFromUpdateEmployeeModel: ...

from datetime import datetime
from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsAssetToAssetServiceForecastModel(BaseModel):
    company_id: StrictInt | None
    asset_id: StrictInt | None
    site_id: StrictInt | None
    asset_service_record_id: StrictInt | None
    serial_number: StrictStr | None
    asset_user: StrictStr | None
    asset_tag: StrictStr | None
    equipment_id: StrictStr | None
    asset_name: StrictStr | None
    category_name: StrictStr | None
    manufacturer_name: StrictStr | None
    site_name: StrictStr | None
    maintenance_plan_id: StrictInt | None
    maintenance_plan_name: StrictStr | None
    maintenance_task_id: StrictInt | None
    maintenance_task_name: StrictStr | None
    next_service_date: datetime | None
    advance_recall_date: datetime | None
    grace_period_date: datetime | None
    certificate_next_service_date: datetime | None
    service_interval: StrictStr | None
    interval_cycle: StrictStr | None
    interval_length: StrictInt | None
    on_day: StrictStr | None
    on_month: StrictStr | None
    on_week_days: StrictStr | None
    weekday_of_month: StrictStr | None
    advance_recall_period: StrictStr | None
    days_before_due: StrictInt | None
    past_due_grace_period: StrictStr | None
    days_after_due: StrictInt | None
    def on_day_validate_enum(cls, value): ...
    def on_month_validate_enum(cls, value): ...
    def on_week_days_validate_enum(cls, value): ...
    def weekday_of_month_validate_enum(cls, value): ...
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsAssetToAssetServiceForecastModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsAssetToAssetServiceForecastModel: ...

from pydantic import BaseModel, StrictBool as StrictBool, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsMaintenancePlansToMaintenanceTaskResponse(BaseModel):
    segment_name: StrictStr | None
    service_level_id: StrictInt | None
    display_order: StrictInt | None
    service_notes: StrictStr | None
    interval_cycle: StrictStr | None
    interval_length: StrictInt | None
    on_day: StrictStr | None
    on_month: StrictStr | None
    on_week_days: StrictStr | None
    weekday_of_month: StrictStr | None
    color_code: StrictInt | None
    service_interval: StrictStr | None
    on_segment_id: StrictInt | None
    document_number: StrictStr | None
    document_section: StrictStr | None
    as_found_standard_group_id: StrictInt | None
    as_left_standard_group_id: StrictInt | None
    task_notes: StrictStr | None
    advance_recall_period: StrictStr | None
    days_before_due: StrictInt | None
    past_due_grace_period: StrictStr | None
    days_after_due: StrictInt | None
    use_period_in_reports: StrictStr | None
    generate_order_automatically: StrictBool | None
    approve_upon_generation: StrictBool | None
    generate_separate: StrictBool | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsMaintenancePlansToMaintenanceTaskResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsMaintenancePlansToMaintenanceTaskResponse: ...

from pydantic import BaseModel, StrictInt as StrictInt, StrictStr as StrictStr

class QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse(BaseModel):
    order_item_id: StrictInt | None
    component_asset_id: StrictInt | None
    component_serial_number: StrictStr | None
    component_asset_tag: StrictStr | None
    component_asset_user: StrictStr | None
    component_equipment_id: StrictStr | None
    component_manufacturer_part_number: StrictStr | None
    component_manufacturer: StrictStr | None
    component_root_category: StrictStr | None
    component_sub_category: StrictStr | None
    component_location: StrictStr | None
    component_display_name: StrictStr | None
    component_display_part_number: StrictStr | None

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse: ...

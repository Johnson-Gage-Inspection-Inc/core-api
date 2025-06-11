from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsReportDatasetsToMeasurementResponse(BaseModel):
    is_accredited: StrictBool | None
    service_total: StrictFloat | StrictInt | None
    repairs_total: StrictFloat | StrictInt | None
    parts_total: StrictFloat | StrictInt | None
    parameter_id: StrictInt | None
    tool_range_name: StrictStr | None
    tool_range_uncertainty: StrictStr | None
    primary_tool_last_service_date: datetime | None
    primary_tool_next_service_date: datetime | None
    primary_tool_calibrated_by: StrictStr | None
    primary_tool_tool_name: StrictStr | None
    primary_tool_tool_description: StrictStr | None
    primary_tool_tool_type_name: StrictStr | None
    primary_tool_manufacturer: StrictStr | None
    primary_tool_manufacturer_part_number: StrictStr | None
    primary_tool_serial_number: StrictStr | None
    secondary_tool_last_service_date: datetime | None
    secondary_tool_next_service_date: datetime | None
    secondary_tool_calibrated_by: StrictStr | None
    secondary_tool_tool_name: StrictStr | None
    secondary_tool_tool_description: StrictStr | None
    secondary_tool_tool_type_name: StrictStr | None
    secondary_tool_manufacturer: StrictStr | None
    secondary_tool_manufacturer_part_number: StrictStr | None
    secondary_tool_serial_number: StrictStr | None
    measurement_set_name: StrictStr | None
    decimal_places: StrictInt | None
    significant_figures: StrictInt | None
    sd_header: StrictFloat | StrictInt | None
    cv_header: StrictFloat | StrictInt | None
    measurement_local_time: datetime | None
    mean: StrictFloat | StrictInt | None
    mean_raw: StrictFloat | StrictInt | None
    mean_decimal_places: StrictInt | None
    mean_extended: StrictStr | None
    sd: StrictFloat | StrictInt | None
    sd_raw: StrictFloat | StrictInt | None
    sd_decimal_places: StrictInt | None
    delta: StrictFloat | StrictInt | None
    range: StrictFloat | StrictInt | None
    sd_extended: StrictStr | None
    range_extended: StrictStr | None
    delta_extended: StrictStr | None
    minimum_measured_value: StrictFloat | StrictInt | None
    maximum_measured_value: StrictFloat | StrictInt | None
    min_max_value_extended: StrictStr | None
    cv: StrictFloat | StrictInt | None
    cv_raw: StrictFloat | StrictInt | None
    cv_decimal_places: StrictInt | None
    cv_extended: StrictStr | None
    result: StrictInt | None
    range_result: StrictBool | None
    delta_result: StrictBool | None
    min_result: StrictBool | None
    max_result: StrictBool | None
    tar_result: StrictBool | None
    tur_result: StrictBool | None
    error_result: StrictBool | None
    sd_result: StrictBool | None
    cv_result: StrictBool | None
    custom_field_result: StrictInt | None
    mu: StrictFloat | StrictInt | None
    mu_raw: StrictFloat | StrictInt | None
    mu_effective_dof: StrictFloat | StrictInt | None
    mu_coverage_factor: StrictFloat | StrictInt | None
    mu_extended: StrictStr | None
    cmc: StrictFloat | StrictInt | None
    cmc_comments: StrictStr | None
    tur: StrictFloat | StrictInt | None
    tur_raw: StrictFloat | StrictInt | None
    tur_decimal_places: StrictInt | None
    tar: StrictFloat | StrictInt | None
    tar_raw: StrictFloat | StrictInt | None
    tar_decimal_places: StrictInt | None
    guard_band: StrictStr | None
    guard_band_logic: StrictStr | None
    uncertainty_budget: StrictStr | None
    calculated_uncertainty: StrictFloat | StrictInt | None
    lock_uncertainty_budget: StrictBool | None
    lab_mu: StrictFloat | StrictInt | None
    channel: StrictInt | None
    measurement_type: StrictStr | None
    updated_by: StrictStr | None
    updated_on: datetime | None
    error: StrictFloat | StrictInt | None
    error_extended: StrictStr | None
    require_adjustment: StrictBool | None
    adjustment_threshold: StrictFloat | StrictInt | None
    percent_of_tolerance: StrictFloat | StrictInt | None
    percent_of_tolerance_extended: StrictStr | None
    tol_decimal_places: StrictInt | None
    specification_title: StrictStr | None
    specification_subtitle: StrictStr | None
    specification_group: StrictStr | None
    batch_type: StrictInt | None
    batch_result: StrictInt | None
    is_by_channel: StrictBool | None
    channel_count: StrictInt | None
    is_range_accredited: StrictBool | None
    commenced_on: datetime | None
    commenced_by: StrictStr | None
    z_factor: StrictFloat | StrictInt | None
    air_buoyancy: StrictFloat | StrictInt | None
    evaporation_rate: StrictFloat | StrictInt | None
    air_humidity: StrictFloat | StrictInt | None
    altitude: StrictFloat | StrictInt | None
    ambient_temperature: StrictFloat | StrictInt | None
    barometric_pressure: StrictFloat | StrictInt | None
    light_intensity: StrictFloat | StrictInt | None
    noise_level: StrictFloat | StrictInt | None
    ph_level: StrictFloat | StrictInt | None
    water_conductivity: StrictFloat | StrictInt | None
    water_temperature: StrictFloat | StrictInt | None
    solar_radiation: StrictFloat | StrictInt | None
    wind_speed: StrictFloat | StrictInt | None
    z_factor_uom: StrictStr | None
    air_buoyancy_uom: StrictStr | None
    evaporation_rate_uom: StrictStr | None
    air_humidity_uom: StrictStr | None
    altitude_uom: StrictStr | None
    ambient_temperature_uom: StrictStr | None
    barometric_pressure_uom: StrictStr | None
    light_intensity_uom: StrictStr | None
    noise_level_uom: StrictStr | None
    ph_level_uom: StrictStr | None
    water_conductivity_uom: StrictStr | None
    water_temperature_uom: StrictStr | None
    solar_radiation_uom: StrictStr | None
    wind_speed_uom: StrictStr | None
    specification_name: StrictStr | None
    parameter_name: StrictStr | None
    measurement_set_display_order: StrictInt | None
    display_order: StrictInt | None
    unit_of_measure: StrictStr | None
    display_format: StrictStr | None
    precision: StrictFloat | StrictInt | None
    minimum: StrictFloat | StrictInt | None
    nominal: StrictFloat | StrictInt | None
    expected_value: StrictFloat | StrictInt | None
    expected_value_raw: StrictStr | None
    test_value: StrictFloat | StrictInt | None
    base_value: StrictFloat | StrictInt | None
    use_expected_value: StrictBool | None
    reading_entry_logic: StrictStr | None
    reading_entry_math: StrictStr | None
    double_substitution_sequence: StrictStr | None
    reading_entry_math_string: StrictStr | None
    nominal_extended: StrictStr | None
    expected_value_extended: StrictStr | None
    maximum: StrictFloat | StrictInt | None
    tolerance_min: StrictFloat | StrictInt | None
    tolerance_max: StrictFloat | StrictInt | None
    resolution: StrictFloat | StrictInt | None
    resolution_count: StrictFloat | StrictInt | None
    min_max_header: StrictStr | None
    accuracy_class: StrictStr | None
    accuracy_class_min: StrictFloat | StrictInt | None
    accuracy_class_max: StrictFloat | StrictInt | None
    environment_mask: StrictStr | None
    display_name: StrictStr | None
    display_part_number: StrictStr | None
    part_number: StrictStr | None
    vendor_company_id: StrictInt | None
    service_order_number: StrictInt | None
    custom_order_number: StrictStr | None
    completed_by_name: StrictStr | None
    completed_on: datetime | None
    is_limited: StrictBool | None
    vendor_tag: StrictStr | None
    vendor_service_notes: StrictStr | None
    room: StrictStr | None
    segment_name: StrictStr | None
    schedule_name: StrictStr | None
    next_segment_name: StrictStr | None
    certificate_number: StrictStr | None
    work_status: StrictInt | None
    service_type: StrictStr | None
    service_level: StrictStr | None
    barcode: StrictStr | None
    service_comments: StrictStr | None
    order_item_number: StrictInt | None
    asset_tag: StrictStr | None
    asset_user: StrictStr | None
    serial_number: StrictStr | None
    equipment_id: StrictStr | None
    legacy_identifier: StrictStr | None
    site_name: StrictStr | None
    asset_name: StrictStr | None
    asset_description: StrictStr | None
    product_name: StrictStr | None
    product_description: StrictStr | None
    asset_maker: StrictStr | None
    station: StrictStr | None
    asset_tag_change: StrictStr | None
    asset_user_change: StrictStr | None
    serial_number_change: StrictStr | None
    service_date: datetime | None
    next_service_date: datetime | None
    service_order_item_id: StrictInt | None
    service_order_id: StrictInt | None
    measurement_batch_id: StrictInt | None
    measurement_id: StrictInt | None
    standard_id: StrictInt | None
    tool_id: StrictInt | None
    measurement_tool_id: StrictInt | None
    measurement_condition_id: StrictInt | None
    measurement_point_id: StrictInt | None
    measurement_set_id: StrictInt | None
    is_hidden: StrictBool | None
    readings: StrictInt | None
    tolerance_type: StrictStr | None
    tolerance_type_string: StrictStr | None
    precision_type: StrictStr | None
    specification_mode: StrictStr | None
    tolerance_mode: StrictStr | None
    tolerance_unit: StrictStr | None
    tolerance_string: StrictStr | None
    po_number: StrictStr | None
    secondary_po: StrictStr | None
    shipped_date: datetime | None
    shipment_status: StrictStr | None
    shipped_on: datetime | None
    delivered_on: datetime | None
    tracking_number: StrictStr | None
    payment_terms: StrictInt | None
    shipping_method: StrictStr | None
    location: StrictStr | None
    site_access_notes: StrictStr | None
    abbreviated_uom: StrictStr | None
    unit_scale_factor: StrictFloat | StrictInt | None
    measurement_not_taken_result: StrictStr | None
    hide_from_certificate: StrictBool | None
    measurement_not_taken_reason: StrictStr | None
    environment_text1: StrictStr | None
    environment_text2: StrictStr | None
    environment_text3: StrictStr | None
    environment_text4: StrictStr | None
    environment_text5: StrictStr | None
    environment_text6: StrictStr | None
    values: StrictStr | None
    value1: StrictStr | None
    value2: StrictStr | None
    value3: StrictStr | None
    value4: StrictStr | None
    value5: StrictStr | None
    value6: StrictStr | None
    value7: StrictStr | None
    value8: StrictStr | None
    value9: StrictStr | None
    value10: StrictStr | None
    value11: StrictStr | None
    value12: StrictStr | None
    value13: StrictStr | None
    value14: StrictStr | None
    value15: StrictStr | None
    value16: StrictStr | None
    value17: StrictStr | None
    value18: StrictStr | None
    value19: StrictStr | None
    value20: StrictStr | None
    value21: StrictStr | None
    value22: StrictStr | None
    value23: StrictStr | None
    value24: StrictStr | None
    value25: StrictStr | None
    value26: StrictStr | None
    value27: StrictStr | None
    value28: StrictStr | None
    value29: StrictStr | None
    value30: StrictStr | None
    value31: StrictStr | None
    value32: StrictStr | None
    value33: StrictStr | None
    value34: StrictStr | None
    value35: StrictStr | None
    value36: StrictStr | None
    value37: StrictStr | None
    value38: StrictStr | None
    value39: StrictStr | None
    value40: StrictStr | None
    raw_value1: StrictStr | None
    raw_value2: StrictStr | None
    raw_value3: StrictStr | None
    raw_value4: StrictStr | None
    raw_value5: StrictStr | None
    raw_value6: StrictStr | None
    raw_value7: StrictStr | None
    raw_value8: StrictStr | None
    raw_value9: StrictStr | None
    raw_value10: StrictStr | None
    raw_value11: StrictStr | None
    raw_value12: StrictStr | None
    raw_value13: StrictStr | None
    raw_value14: StrictStr | None
    raw_value15: StrictStr | None
    raw_value16: StrictStr | None
    raw_value17: StrictStr | None
    raw_value18: StrictStr | None
    raw_value19: StrictStr | None
    raw_value20: StrictStr | None
    raw_value21: StrictStr | None
    raw_value22: StrictStr | None
    raw_value23: StrictStr | None
    raw_value24: StrictStr | None
    raw_value25: StrictStr | None
    raw_value26: StrictStr | None
    raw_value27: StrictStr | None
    raw_value28: StrictStr | None
    raw_value29: StrictStr | None
    raw_value30: StrictStr | None
    raw_value31: StrictStr | None
    raw_value32: StrictStr | None
    raw_value33: StrictStr | None
    raw_value34: StrictStr | None
    raw_value35: StrictStr | None
    raw_value36: StrictStr | None
    raw_value37: StrictStr | None
    raw_value38: StrictStr | None
    raw_value39: StrictStr | None
    raw_value40: StrictStr | None
    subtitles_to_readings: StrictStr | None
    value_subtitle1: StrictStr | None
    value_subtitle2: StrictStr | None
    value_subtitle3: StrictStr | None
    value_subtitle4: StrictStr | None
    value_subtitle5: StrictStr | None
    value_subtitle6: StrictStr | None
    value_subtitle7: StrictStr | None
    value_subtitle8: StrictStr | None
    value_subtitle9: StrictStr | None
    value_subtitle10: StrictStr | None
    value_subtitle11: StrictStr | None
    value_subtitle12: StrictStr | None
    value_subtitle13: StrictStr | None
    value_subtitle14: StrictStr | None
    value_subtitle15: StrictStr | None
    value_subtitle16: StrictStr | None
    value_subtitle17: StrictStr | None
    value_subtitle18: StrictStr | None
    value_subtitle19: StrictStr | None
    value_subtitle20: StrictStr | None
    value_subtitle21: StrictStr | None
    value_subtitle22: StrictStr | None
    value_subtitle23: StrictStr | None
    value_subtitle24: StrictStr | None
    value_subtitle25: StrictStr | None
    value_subtitle26: StrictStr | None
    value_subtitle27: StrictStr | None
    value_subtitle28: StrictStr | None
    value_subtitle29: StrictStr | None
    value_subtitle30: StrictStr | None
    value_subtitle31: StrictStr | None
    value_subtitle32: StrictStr | None
    value_subtitle33: StrictStr | None
    value_subtitle34: StrictStr | None
    value_subtitle35: StrictStr | None
    value_subtitle36: StrictStr | None
    value_subtitle37: StrictStr | None
    value_subtitle38: StrictStr | None
    value_subtitle39: StrictStr | None
    value_subtitle40: StrictStr | None
    values_decimal_places: StrictInt | None
    repeat_measurement_and_calculate_hysteresis: StrictBool | None
    measurement_point_order: StrictStr | None
    hysteresis_point: StrictStr | None
    max_hysteresis: StrictFloat | StrictInt | None
    run: StrictInt | None
    direction: StrictInt | None
    hysteresis: StrictFloat | StrictInt | None
    column_mean: StrictStr | None
    column_mean_result: StrictStr | None
    column_sd: StrictStr | None
    column_sd_result: StrictStr | None
    column_cv: StrictStr | None
    column_cv_result: StrictStr | None
    column_range: StrictStr | None
    column_range_result: StrictStr | None
    column_delta: StrictStr | None
    column_delta_result: StrictStr | None
    column_result: StrictStr | None
    def guard_band_logic_validate_enum(cls, value): ...
    def measurement_type_validate_enum(cls, value): ...
    def reading_entry_logic_validate_enum(cls, value): ...
    def reading_entry_math_validate_enum(cls, value): ...
    def double_substitution_sequence_validate_enum(cls, value): ...
    def environment_mask_validate_enum(cls, value): ...
    def tolerance_type_validate_enum(cls, value): ...
    def precision_type_validate_enum(cls, value): ...
    def specification_mode_validate_enum(cls, value): ...
    def tolerance_mode_validate_enum(cls, value): ...
    def tolerance_unit_validate_enum(cls, value): ...
    def shipment_status_validate_enum(cls, value): ...
    def measurement_not_taken_result_validate_enum(cls, value): ...
    def measurement_point_order_validate_enum(cls, value): ...
    def hysteresis_point_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToMeasurementResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToMeasurementResponse: ...

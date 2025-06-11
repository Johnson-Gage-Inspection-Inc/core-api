from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
)

class QualerApiModelsReportDatasetsToMeasurementAllResponse(BaseModel):
    barcode: StrictStr | None
    display_name: StrictStr | None
    display_part_number: StrictStr | None
    part_number: StrictStr | None
    vendor_company_id: StrictInt | None
    service_order_number: StrictInt | None
    completed_by_name: StrictStr | None
    completed_on: datetime | None
    is_limited: StrictBool | None
    vendor_tag: StrictStr | None
    room: StrictStr | None
    segment_name: StrictStr | None
    schedule_name: StrictStr | None
    next_segment_name: StrictStr | None
    certificate_number: StrictStr | None
    work_status: StrictInt | None
    service_type: StrictStr | None
    service_level: StrictStr | None
    service_comments: StrictStr | None
    order_item_number: StrictInt | None
    service_total: StrictFloat | StrictInt | None
    repairs_total: StrictFloat | StrictInt | None
    parts_total: StrictFloat | StrictInt | None
    asset_tag: StrictStr | None
    asset_user: StrictStr | None
    serial_number: StrictStr | None
    equipment_id: StrictStr | None
    legacy_identifier: StrictStr | None
    asset_name: StrictStr | None
    asset_description: StrictStr | None
    product_name: StrictStr | None
    product_description: StrictStr | None
    asset_maker: StrictStr | None
    asset_tag_change: StrictStr | None
    asset_user_change: StrictStr | None
    serial_number_change: StrictStr | None
    service_date: datetime | None
    next_service_date: datetime | None
    service_order_item_id: StrictInt | None
    site_name: StrictStr | None
    po_number: StrictStr | None
    shipped_date: datetime | None
    tracking_number: StrictStr | None
    payment_terms: StrictInt | None
    shipping_method: StrictStr | None
    location: StrictStr | None
    site_access_notes: StrictStr | None
    as_left_decimal_places: StrictInt | None
    as_left_measurement_set_name: StrictStr | None
    as_left_measurement_set_id: StrictInt | None
    as_left_adjustment_threshold: StrictFloat | StrictInt | None
    as_left_mean_extended: StrictStr | None
    as_left_sd_extended: StrictStr | None
    as_left_range_extended: StrictStr | None
    as_left_delta_extended: StrictStr | None
    as_left_cv_extended: StrictStr | None
    as_left_nominal_extended: StrictStr | None
    as_left_min_max_header: StrictStr | None
    as_left_accuracy_class: StrictStr | None
    as_left_accuracy_class_min: StrictFloat | StrictInt | None
    as_left_accuracy_class_max: StrictFloat | StrictInt | None
    as_left_minimum_measured_value: StrictFloat | StrictInt | None
    as_left_maxi_mum_measured_value: StrictFloat | StrictInt | None
    as_left_min_max_value_extended: StrictStr | None
    as_left_tool_range_name: StrictStr | None
    as_left_tool_range_uncertainty: StrictStr | None
    as_left_primary_tool_last_service_date: datetime | None
    as_left_primary_tool_next_service_date: datetime | None
    as_left_primary_tool_calibrated_by: StrictStr | None
    as_left_primary_tool_tool_name: StrictStr | None
    as_left_primary_tool_tool_description: StrictStr | None
    as_left_primary_tool_tool_type_name: StrictStr | None
    as_left_primary_tool_manufacturer: StrictStr | None
    as_left_primary_tool_manufacturer_part_number: StrictStr | None
    as_left_primary_tool_serial_number: StrictStr | None
    as_found_measurement_set_name: StrictStr | None
    as_found_measurement_set_id: StrictInt | None
    as_found_adjustment_threshold: StrictFloat | StrictInt | None
    as_found_decimal_places: StrictInt | None
    as_found_mean_extended: StrictStr | None
    as_found_sd_extended: StrictStr | None
    as_found_range_extended: StrictStr | None
    as_found_delta_extended: StrictStr | None
    as_found_cv_extended: StrictStr | None
    as_found_nominal_extended: StrictStr | None
    as_found_min_max_header: StrictStr | None
    as_found_accuracy_class: StrictStr | None
    as_found_accuracy_class_min: StrictFloat | StrictInt | None
    as_found_accuracy_class_max: StrictFloat | StrictInt | None
    as_found_minimum_measured_value: StrictFloat | StrictInt | None
    as_found_maxi_mum_measured_value: StrictFloat | StrictInt | None
    as_found_min_max_value_extended: StrictStr | None
    as_found_tool_range_name: StrictStr | None
    as_found_tool_range_uncertainty: StrictStr | None
    as_found_primary_tool_last_service_date: datetime | None
    as_found_primary_tool_next_service_date: datetime | None
    as_found_primary_tool_calibrated_by: StrictStr | None
    as_found_primary_tool_tool_name: StrictStr | None
    as_found_primary_tool_tool_description: StrictStr | None
    as_found_primary_tool_tool_type_name: StrictStr | None
    as_found_primary_tool_manufacturer: StrictStr | None
    as_found_primary_tool_manufacturer_part_number: StrictStr | None
    as_found_primary_tool_serial_number: StrictStr | None
    as_left_secondary_tool_last_service_date: datetime | None
    as_left_secondary_tool_next_service_date: datetime | None
    as_left_secondary_tool_calibrated_by: StrictStr | None
    as_left_secondary_tool_tool_name: StrictStr | None
    as_left_secondary_tool_tool_description: StrictStr | None
    as_left_secondary_tool_tool_type_name: StrictStr | None
    as_left_secondary_tool_manufacturer: StrictStr | None
    as_left_secondary_tool_manufacturer_part_number: StrictStr | None
    as_left_secondary_tool_serial_number: StrictStr | None
    as_found_secondary_tool_last_service_date: datetime | None
    as_found_secondary_tool_next_service_date: datetime | None
    as_found_secondary_tool_calibrated_by: StrictStr | None
    as_found_secondary_tool_tool_name: StrictStr | None
    as_found_secondary_tool_tool_description: StrictStr | None
    as_found_secondary_tool_tool_type_name: StrictStr | None
    as_found_secondary_tool_manufacturer: StrictStr | None
    as_found_secondary_tool_manufacturer_part_number: StrictStr | None
    as_found_secondary_tool_serial_number: StrictStr | None
    as_found_measurement_not_taken_result: StrictStr | None
    as_found_hide_from_certificate: StrictBool | None
    as_found_measurement_not_taken_reason: StrictStr | None
    as_left_values: StrictStr | None
    as_left_is_accredited: StrictBool | None
    as_left_is_range_accredited: StrictBool | None
    as_found_values: StrictStr | None
    as_found_is_accredited: StrictBool | None
    as_found_is_range_accredited: StrictBool | None
    as_found_parameter_id: StrictInt | None
    as_found_sd_header: StrictFloat | StrictInt | None
    as_found_cv_header: StrictFloat | StrictInt | None
    as_found_measurement_local_time: datetime | None
    as_found_tur: StrictFloat | StrictInt | None
    as_found_tur_raw: StrictFloat | StrictInt | None
    as_left_tur: StrictFloat | StrictInt | None
    as_left_tur_raw: StrictFloat | StrictInt | None
    as_found_tar: StrictFloat | StrictInt | None
    as_found_tar_raw: StrictFloat | StrictInt | None
    as_left_tar: StrictFloat | StrictInt | None
    as_left_tar_raw: StrictFloat | StrictInt | None
    as_found_guard_band: StrictStr | None
    as_left_guard_band: StrictStr | None
    as_found_guard_band_logic: StrictStr | None
    as_left_guard_band_logic: StrictStr | None
    as_found_error: StrictFloat | StrictInt | None
    as_found_error_extended: StrictStr | None
    as_left_error: StrictFloat | StrictInt | None
    as_left_error_extended: StrictStr | None
    as_found_percent_of_tolerance: StrictFloat | StrictInt | None
    as_found_percent_of_tolerance_extended: StrictStr | None
    as_left_percent_of_tolerance: StrictFloat | StrictInt | None
    as_left_percent_of_tolerance_extended: StrictStr | None
    as_found_tolerance_maximum: StrictFloat | StrictInt | None
    as_found_tolerance_minimum: StrictFloat | StrictInt | None
    as_found_tolerance_type: StrictInt | None
    as_found_tolerance_mode: StrictInt | None
    as_found_tolerance_string: StrictStr | None
    as_left_tolerance_maximum: StrictFloat | StrictInt | None
    as_left_tolerance_minimum: StrictFloat | StrictInt | None
    as_left_tolerance_type: StrictInt | None
    as_left_tolerance_mode: StrictInt | None
    as_left_tolerance_string: StrictStr | None
    as_found_max_hysteresis: StrictFloat | StrictInt | None
    as_found_run: StrictInt | None
    as_found_direction: StrictInt | None
    as_found_hysteresis: StrictFloat | StrictInt | None
    as_left_max_hysteresis: StrictFloat | StrictInt | None
    as_left_run: StrictInt | None
    as_left_direction: StrictInt | None
    as_left_hysteresis: StrictFloat | StrictInt | None
    as_found_reading_entry_math: StrictStr | None
    as_found_reading_entry_math_string: StrictStr | None
    as_found_value1: StrictStr | None
    as_found_value2: StrictStr | None
    as_found_value3: StrictStr | None
    as_found_value4: StrictStr | None
    as_found_value5: StrictStr | None
    as_found_value6: StrictStr | None
    as_found_value7: StrictStr | None
    as_found_value8: StrictStr | None
    as_found_value9: StrictStr | None
    as_found_value10: StrictStr | None
    as_found_value11: StrictStr | None
    as_found_value12: StrictStr | None
    as_found_value13: StrictStr | None
    as_found_value14: StrictStr | None
    as_found_value15: StrictStr | None
    as_found_value16: StrictStr | None
    as_found_value17: StrictStr | None
    as_found_value18: StrictStr | None
    as_found_value19: StrictStr | None
    as_found_value20: StrictStr | None
    as_found_value21: StrictStr | None
    as_found_value22: StrictStr | None
    as_found_value23: StrictStr | None
    as_found_value24: StrictStr | None
    as_found_value25: StrictStr | None
    as_found_value26: StrictStr | None
    as_found_value27: StrictStr | None
    as_found_value28: StrictStr | None
    as_found_value29: StrictStr | None
    as_found_value30: StrictStr | None
    as_found_value31: StrictStr | None
    as_found_value32: StrictStr | None
    as_found_value33: StrictStr | None
    as_found_value34: StrictStr | None
    as_found_value35: StrictStr | None
    as_found_value36: StrictStr | None
    as_found_value37: StrictStr | None
    as_found_value38: StrictStr | None
    as_found_value39: StrictStr | None
    as_found_value40: StrictStr | None
    as_found_raw_value1: StrictStr | None
    as_found_raw_value2: StrictStr | None
    as_found_raw_value3: StrictStr | None
    as_found_raw_value4: StrictStr | None
    as_found_raw_value5: StrictStr | None
    as_found_raw_value6: StrictStr | None
    as_found_raw_value7: StrictStr | None
    as_found_raw_value8: StrictStr | None
    as_found_raw_value9: StrictStr | None
    as_found_raw_value10: StrictStr | None
    as_found_raw_value11: StrictStr | None
    as_found_raw_value12: StrictStr | None
    as_found_raw_value13: StrictStr | None
    as_found_raw_value14: StrictStr | None
    as_found_raw_value15: StrictStr | None
    as_found_raw_value16: StrictStr | None
    as_found_raw_value17: StrictStr | None
    as_found_raw_value18: StrictStr | None
    as_found_raw_value19: StrictStr | None
    as_found_raw_value20: StrictStr | None
    as_found_raw_value21: StrictStr | None
    as_found_raw_value22: StrictStr | None
    as_found_raw_value23: StrictStr | None
    as_found_raw_value24: StrictStr | None
    as_found_raw_value25: StrictStr | None
    as_found_raw_value26: StrictStr | None
    as_found_raw_value27: StrictStr | None
    as_found_raw_value28: StrictStr | None
    as_found_raw_value29: StrictStr | None
    as_found_raw_value30: StrictStr | None
    as_found_raw_value31: StrictStr | None
    as_found_raw_value32: StrictStr | None
    as_found_raw_value33: StrictStr | None
    as_found_raw_value34: StrictStr | None
    as_found_raw_value35: StrictStr | None
    as_found_raw_value36: StrictStr | None
    as_found_raw_value37: StrictStr | None
    as_found_raw_value38: StrictStr | None
    as_found_raw_value39: StrictStr | None
    as_found_raw_value40: StrictStr | None
    as_found_value_subtitle1: StrictStr | None
    as_found_value_subtitle2: StrictStr | None
    as_found_value_subtitle3: StrictStr | None
    as_found_value_subtitle4: StrictStr | None
    as_found_value_subtitle5: StrictStr | None
    as_found_value_subtitle6: StrictStr | None
    as_found_value_subtitle7: StrictStr | None
    as_found_value_subtitle8: StrictStr | None
    as_found_value_subtitle9: StrictStr | None
    as_found_value_subtitle10: StrictStr | None
    as_found_value_subtitle11: StrictStr | None
    as_found_value_subtitle12: StrictStr | None
    as_found_value_subtitle13: StrictStr | None
    as_found_value_subtitle14: StrictStr | None
    as_found_value_subtitle15: StrictStr | None
    as_found_value_subtitle16: StrictStr | None
    as_found_value_subtitle17: StrictStr | None
    as_found_value_subtitle18: StrictStr | None
    as_found_value_subtitle19: StrictStr | None
    as_found_value_subtitle20: StrictStr | None
    as_found_value_subtitle21: StrictStr | None
    as_found_value_subtitle22: StrictStr | None
    as_found_value_subtitle23: StrictStr | None
    as_found_value_subtitle24: StrictStr | None
    as_found_value_subtitle25: StrictStr | None
    as_found_value_subtitle26: StrictStr | None
    as_found_value_subtitle27: StrictStr | None
    as_found_value_subtitle28: StrictStr | None
    as_found_value_subtitle29: StrictStr | None
    as_found_value_subtitle30: StrictStr | None
    as_found_value_subtitle31: StrictStr | None
    as_found_value_subtitle32: StrictStr | None
    as_found_value_subtitle33: StrictStr | None
    as_found_value_subtitle34: StrictStr | None
    as_found_value_subtitle35: StrictStr | None
    as_found_value_subtitle36: StrictStr | None
    as_found_value_subtitle37: StrictStr | None
    as_found_value_subtitle38: StrictStr | None
    as_found_value_subtitle39: StrictStr | None
    as_found_value_subtitle40: StrictStr | None
    as_found_mean: StrictFloat | StrictInt | None
    as_found_mean_raw: StrictFloat | StrictInt | None
    as_found_sd: StrictFloat | StrictInt | None
    as_found_sd_raw: StrictFloat | StrictInt | None
    as_found_delta: StrictFloat | StrictInt | None
    as_found_range: StrictFloat | StrictInt | None
    as_found_cv: StrictFloat | StrictInt | None
    as_found_cv_raw: StrictFloat | StrictInt | None
    as_found_result: StrictInt | None
    as_found_range_result: StrictBool | None
    as_found_delta_result: StrictBool | None
    as_found_min_result: StrictBool | None
    as_found_max_result: StrictBool | None
    as_found_tar_result: StrictBool | None
    as_found_tur_result: StrictBool | None
    as_found_error_result: StrictBool | None
    as_found_sd_result: StrictBool | None
    as_found_cv_result: StrictBool | None
    as_found_custom_field_result: StrictInt | None
    as_found_mu: StrictFloat | StrictInt | None
    as_found_mu_raw: StrictFloat | StrictInt | None
    as_found_mu_effective_dof: StrictFloat | StrictInt | None
    as_found_mu_coverage_factor: StrictFloat | StrictInt | None
    as_found_cmc: StrictFloat | StrictInt | None
    as_found_cmc_comments: StrictStr | None
    as_found_calculated_uncertainty: StrictFloat | StrictInt | None
    as_found_lab_mu: StrictFloat | StrictInt | None
    as_found_uncertainty_budget: StrictStr | None
    as_found_mu_extended: StrictStr | None
    as_found_channel: StrictInt | None
    as_found_measurement_type: StrictStr | None
    as_found_updated_by: StrictStr | None
    as_found_updated_on: datetime | None
    as_left_abbreviated_uom: StrictStr | None
    as_left_unit_scale_factor: StrictFloat | StrictInt | None
    as_found_specification_title: StrictStr | None
    as_found_specification_subtitle: StrictStr | None
    as_found_specification_group: StrictStr | None
    as_found_batch_type: StrictInt | None
    as_found_batch_result: StrictInt | None
    as_found_is_by_channel: StrictBool | None
    as_found_channel_count: StrictInt | None
    as_found_commenced_on: datetime | None
    as_found_commenced_by: StrictStr | None
    as_found_z_factor: StrictFloat | StrictInt | None
    as_found_air_buoyancy: StrictFloat | StrictInt | None
    as_found_evaporation_rate: StrictFloat | StrictInt | None
    as_found_ambient_temperature: StrictFloat | StrictInt | None
    as_found_air_humidity: StrictFloat | StrictInt | None
    as_found_barometric_pressure: StrictFloat | StrictInt | None
    as_found_altitude: StrictFloat | StrictInt | None
    as_found_wind_speed: StrictFloat | StrictInt | None
    as_found_solar_radiation: StrictFloat | StrictInt | None
    as_found_light_intensity: StrictFloat | StrictInt | None
    as_found_noise_level: StrictFloat | StrictInt | None
    as_found_ph_level: StrictFloat | StrictInt | None
    as_found_water_conductivity: StrictFloat | StrictInt | None
    as_found_water_temperature: StrictFloat | StrictInt | None
    as_found_z_factor_uom: StrictStr | None
    as_found_air_buoyancy_uom: StrictStr | None
    as_found_evaporation_rate_uom: StrictStr | None
    as_found_ambient_temperature_uom: StrictStr | None
    as_found_air_humidity_uom: StrictStr | None
    as_found_barometric_pressure_uom: StrictStr | None
    as_found_altitude_uom: StrictStr | None
    as_found_wind_speed_uom: StrictStr | None
    as_found_solar_radiation_uom: StrictStr | None
    as_found_light_intensity_uom: StrictStr | None
    as_found_noise_level_uom: StrictStr | None
    as_found_ph_level_uom: StrictStr | None
    as_found_water_conductivity_uom: StrictStr | None
    as_found_water_temperature_uom: StrictStr | None
    as_found_abbreviated_uom: StrictStr | None
    as_found_unit_scale_factor: StrictFloat | StrictInt | None
    as_found_specification_name: StrictStr | None
    as_found_parameter_name: StrictStr | None
    as_found_display_order: StrictInt | None
    as_found_unit_of_measure: StrictStr | None
    as_found_display_format: StrictStr | None
    as_found_precision: StrictFloat | StrictInt | None
    as_found_precision_type: StrictStr | None
    as_found_minimum: StrictFloat | StrictInt | None
    as_found_nominal: StrictFloat | StrictInt | None
    as_found_expected_value: StrictFloat | StrictInt | None
    as_found_expected_value_raw: StrictStr | None
    as_found_test_value: StrictFloat | StrictInt | None
    as_found_base_value: StrictFloat | StrictInt | None
    as_found_maxi_mum: StrictFloat | StrictInt | None
    as_found_resolution: StrictFloat | StrictInt | None
    as_found_resolution_count: StrictInt | None
    as_found_measurement_batch_id: StrictInt | None
    as_found_measurement_id: StrictInt | None
    as_found_standard_id: StrictInt | None
    as_found_tool_id: StrictInt | None
    as_found_measurement_condition_id: StrictInt | None
    as_found_measurement_point_id: StrictInt | None
    as_left_parameter_id: StrictInt | None
    as_left_sd_header: StrictFloat | StrictInt | None
    as_left_cv_header: StrictFloat | StrictInt | None
    as_left_measurement_local_time: datetime | None
    as_left_reading_entry_math: StrictStr | None
    as_left_reading_entry_math_string: StrictStr | None
    as_left_value1: StrictStr | None
    as_left_value2: StrictStr | None
    as_left_value3: StrictStr | None
    as_left_value4: StrictStr | None
    as_left_value5: StrictStr | None
    as_left_value6: StrictStr | None
    as_left_value7: StrictStr | None
    as_left_value8: StrictStr | None
    as_left_value9: StrictStr | None
    as_left_value10: StrictStr | None
    as_left_value11: StrictStr | None
    as_left_value12: StrictStr | None
    as_left_value13: StrictStr | None
    as_left_value14: StrictStr | None
    as_left_value15: StrictStr | None
    as_left_value16: StrictStr | None
    as_left_value17: StrictStr | None
    as_left_value18: StrictStr | None
    as_left_value19: StrictStr | None
    as_left_value20: StrictStr | None
    as_left_value21: StrictStr | None
    as_left_value22: StrictStr | None
    as_left_value23: StrictStr | None
    as_left_value24: StrictStr | None
    as_left_value25: StrictStr | None
    as_left_value26: StrictStr | None
    as_left_value27: StrictStr | None
    as_left_value28: StrictStr | None
    as_left_value29: StrictStr | None
    as_left_value30: StrictStr | None
    as_left_value31: StrictStr | None
    as_left_value32: StrictStr | None
    as_left_value33: StrictStr | None
    as_left_value34: StrictStr | None
    as_left_value35: StrictStr | None
    as_left_value36: StrictStr | None
    as_left_value37: StrictStr | None
    as_left_value38: StrictStr | None
    as_left_value39: StrictStr | None
    as_left_value40: StrictStr | None
    as_left_raw_value1: StrictStr | None
    as_left_raw_value2: StrictStr | None
    as_left_raw_value3: StrictStr | None
    as_left_raw_value4: StrictStr | None
    as_left_raw_value5: StrictStr | None
    as_left_raw_value6: StrictStr | None
    as_left_raw_value7: StrictStr | None
    as_left_raw_value8: StrictStr | None
    as_left_raw_value9: StrictStr | None
    as_left_raw_value10: StrictStr | None
    as_left_raw_value11: StrictStr | None
    as_left_raw_value12: StrictStr | None
    as_left_raw_value13: StrictStr | None
    as_left_raw_value14: StrictStr | None
    as_left_raw_value15: StrictStr | None
    as_left_raw_value16: StrictStr | None
    as_left_raw_value17: StrictStr | None
    as_left_raw_value18: StrictStr | None
    as_left_raw_value19: StrictStr | None
    as_left_raw_value20: StrictStr | None
    as_left_raw_value21: StrictStr | None
    as_left_raw_value22: StrictStr | None
    as_left_raw_value23: StrictStr | None
    as_left_raw_value24: StrictStr | None
    as_left_raw_value25: StrictStr | None
    as_left_raw_value26: StrictStr | None
    as_left_raw_value27: StrictStr | None
    as_left_raw_value28: StrictStr | None
    as_left_raw_value29: StrictStr | None
    as_left_raw_value30: StrictStr | None
    as_left_raw_value31: StrictStr | None
    as_left_raw_value32: StrictStr | None
    as_left_raw_value33: StrictStr | None
    as_left_raw_value34: StrictStr | None
    as_left_raw_value35: StrictStr | None
    as_left_raw_value36: StrictStr | None
    as_left_raw_value37: StrictStr | None
    as_left_raw_value38: StrictStr | None
    as_left_raw_value39: StrictStr | None
    as_left_raw_value40: StrictStr | None
    as_left_value_subtitle1: StrictStr | None
    as_left_value_subtitle2: StrictStr | None
    as_left_value_subtitle3: StrictStr | None
    as_left_value_subtitle4: StrictStr | None
    as_left_value_subtitle5: StrictStr | None
    as_left_value_subtitle6: StrictStr | None
    as_left_value_subtitle7: StrictStr | None
    as_left_value_subtitle8: StrictStr | None
    as_left_value_subtitle9: StrictStr | None
    as_left_value_subtitle10: StrictStr | None
    as_left_value_subtitle11: StrictStr | None
    as_left_value_subtitle12: StrictStr | None
    as_left_value_subtitle13: StrictStr | None
    as_left_value_subtitle14: StrictStr | None
    as_left_value_subtitle15: StrictStr | None
    as_left_value_subtitle16: StrictStr | None
    as_left_value_subtitle17: StrictStr | None
    as_left_value_subtitle18: StrictStr | None
    as_left_value_subtitle19: StrictStr | None
    as_left_value_subtitle20: StrictStr | None
    as_left_value_subtitle21: StrictStr | None
    as_left_value_subtitle22: StrictStr | None
    as_left_value_subtitle23: StrictStr | None
    as_left_value_subtitle24: StrictStr | None
    as_left_value_subtitle25: StrictStr | None
    as_left_value_subtitle26: StrictStr | None
    as_left_value_subtitle27: StrictStr | None
    as_left_value_subtitle28: StrictStr | None
    as_left_value_subtitle29: StrictStr | None
    as_left_value_subtitle30: StrictStr | None
    as_left_value_subtitle31: StrictStr | None
    as_left_value_subtitle32: StrictStr | None
    as_left_value_subtitle33: StrictStr | None
    as_left_value_subtitle34: StrictStr | None
    as_left_value_subtitle35: StrictStr | None
    as_left_value_subtitle36: StrictStr | None
    as_left_value_subtitle37: StrictStr | None
    as_left_value_subtitle38: StrictStr | None
    as_left_value_subtitle39: StrictStr | None
    as_left_value_subtitle40: StrictStr | None
    as_left_mean: StrictFloat | StrictInt | None
    as_left_mean_raw: StrictFloat | StrictInt | None
    as_left_sd: StrictFloat | StrictInt | None
    as_left_sd_raw: StrictFloat | StrictInt | None
    as_left_cv: StrictFloat | StrictInt | None
    as_left_cv_raw: StrictFloat | StrictInt | None
    as_left_delta: StrictFloat | StrictInt | None
    as_left_range: StrictFloat | StrictInt | None
    as_left_result: StrictInt | None
    as_left_range_result: StrictBool | None
    as_left_delta_result: StrictBool | None
    as_left_min_result: StrictBool | None
    as_left_max_result: StrictBool | None
    as_left_tar_result: StrictBool | None
    as_left_tur_result: StrictBool | None
    as_left_error_result: StrictBool | None
    as_left_sd_result: StrictBool | None
    as_left_cv_result: StrictBool | None
    as_left_custom_field_result: StrictInt | None
    as_left_mu: StrictFloat | StrictInt | None
    as_left_mu_raw: StrictFloat | StrictInt | None
    as_left_mu_effective_dof: StrictFloat | StrictInt | None
    as_left_mu_coverage_factor: StrictFloat | StrictInt | None
    as_left_cmc: StrictFloat | StrictInt | None
    as_left_cmc_comments: StrictStr | None
    as_left_calculated_uncertainty: StrictFloat | StrictInt | None
    as_left_lab_mu: StrictFloat | StrictInt | None
    as_left_uncertainty_budget: StrictStr | None
    as_left_mu_extended: StrictStr | None
    as_left_channel: StrictInt | None
    as_left_measurement_type: StrictStr | None
    as_left_updated_by: StrictStr | None
    as_left_updated_on: datetime | None
    as_left_specification_title: StrictStr | None
    as_left_specification_subtitle: StrictStr | None
    as_left_specification_group: StrictStr | None
    as_left_batch_type: StrictInt | None
    as_left_batch_result: StrictInt | None
    as_left_is_by_channel: StrictBool | None
    as_left_channel_count: StrictInt | None
    as_left_commenced_on: datetime | None
    as_left_commenced_by: StrictStr | None
    as_left_z_factor: StrictFloat | StrictInt | None
    as_left_air_buoyancy: StrictFloat | StrictInt | None
    as_left_evaporation_rate: StrictFloat | StrictInt | None
    as_left_ambient_temperature: StrictFloat | StrictInt | None
    as_left_air_humidity: StrictFloat | StrictInt | None
    as_left_barometric_pressure: StrictFloat | StrictInt | None
    as_left_altitude: StrictFloat | StrictInt | None
    as_left_wind_speed: StrictFloat | StrictInt | None
    as_left_solar_radiation: StrictFloat | StrictInt | None
    as_left_light_intensity: StrictFloat | StrictInt | None
    as_left_noise_level: StrictFloat | StrictInt | None
    as_left_ph_level: StrictFloat | StrictInt | None
    as_left_water_conductivity: StrictFloat | StrictInt | None
    as_left_water_temperature: StrictFloat | StrictInt | None
    as_left_z_factor_uom: StrictStr | None
    as_left_air_buoyancy_uom: StrictStr | None
    as_left_evaporation_rate_uom: StrictStr | None
    as_left_ambient_temperature_uom: StrictStr | None
    as_left_air_humidity_uom: StrictStr | None
    as_left_barometric_pressure_uom: StrictStr | None
    as_left_altitude_uom: StrictStr | None
    as_left_wind_speed_uom: StrictStr | None
    as_left_solar_radiation_uom: StrictStr | None
    as_left_light_intensity_uom: StrictStr | None
    as_left_noise_level_uom: StrictStr | None
    as_left_ph_level_uom: StrictStr | None
    as_left_water_conductivity_uom: StrictStr | None
    as_left_water_temperature_uom: StrictStr | None
    as_left_specification_name: StrictStr | None
    as_left_parameter_name: StrictStr | None
    as_left_display_order: StrictInt | None
    as_left_unit_of_measure: StrictStr | None
    as_left_display_format: StrictStr | None
    as_left_precision: StrictFloat | StrictInt | None
    as_left_precision_type: StrictStr | None
    as_left_minimum: StrictFloat | StrictInt | None
    as_left_nominal: StrictFloat | StrictInt | None
    as_left_expected_value: StrictFloat | StrictInt | None
    as_left_expected_value_raw: StrictStr | None
    as_left_test_value: StrictFloat | StrictInt | None
    as_left_base_value: StrictFloat | StrictInt | None
    as_left_maxi_mum: StrictFloat | StrictInt | None
    as_left_resolution: StrictFloat | StrictInt | None
    as_left_resolution_count: StrictInt | None
    as_left_measurement_not_taken_result: StrictStr | None
    as_left_hide_from_certificate: StrictBool | None
    as_left_measurement_not_taken_reason: StrictStr | None
    as_left_measurement_batch_id: StrictInt | None
    as_left_measurement_id: StrictInt | None
    as_left_standard_id: StrictInt | None
    as_left_tool_id: StrictInt | None
    as_left_measurement_condition_id: StrictInt | None
    as_left_measurement_point_id: StrictInt | None
    def as_found_measurement_not_taken_result_validate_enum(cls, value): ...
    def as_found_guard_band_logic_validate_enum(cls, value): ...
    def as_left_guard_band_logic_validate_enum(cls, value): ...
    def as_found_reading_entry_math_validate_enum(cls, value): ...
    def as_found_measurement_type_validate_enum(cls, value): ...
    def as_found_precision_type_validate_enum(cls, value): ...
    def as_left_reading_entry_math_validate_enum(cls, value): ...
    def as_left_measurement_type_validate_enum(cls, value): ...
    def as_left_precision_type_validate_enum(cls, value): ...
    def as_left_measurement_not_taken_result_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToMeasurementAllResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToMeasurementAllResponse: ...

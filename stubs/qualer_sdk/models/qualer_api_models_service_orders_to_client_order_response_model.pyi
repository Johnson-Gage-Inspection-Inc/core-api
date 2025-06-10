from datetime import datetime
from pydantic import BaseModel, StrictBool as StrictBool, StrictFloat as StrictFloat, StrictInt as StrictInt, StrictStr as StrictStr
from qualer_sdk.models.qualer_api_models_address_to_address_response_model import QualerApiModelsAddressToAddressResponseModel as QualerApiModelsAddressToAddressResponseModel

class QualerApiModelsServiceOrdersToClientOrderResponseModel(BaseModel):
    service_order_id: StrictInt | None
    parent_order_id: StrictInt | None
    client_legacy_id: StrictStr | None
    owner_name: StrictStr | None
    submited_by_name: StrictStr | None
    sign_off_by_name: StrictStr | None
    vendor_sign_off_by_name: StrictStr | None
    approved_by_name: StrictStr | None
    accepted_by_name: StrictStr | None
    ready_for_quality_control_by_name: StrictStr | None
    quality_control_by_name: StrictStr | None
    created_by_name: StrictStr | None
    completed_by_name: StrictStr | None
    shipped_by_name: StrictStr | None
    delivered_by_name: StrictStr | None
    invoiced_by_name: StrictStr | None
    paid_by_name: StrictStr | None
    cancelled_by_name: StrictStr | None
    closed_by_name: StrictStr | None
    client_company_id: StrictInt | None
    client_company_name: StrictStr | None
    client_domain_name: StrictStr | None
    client_alternative_names: StrictStr | None
    service_comments: StrictStr | None
    service_private_comments: StrictStr | None
    created_on: datetime | None
    approved_on: datetime | None
    sign_off_on: datetime | None
    vendor_sign_off_on: datetime | None
    completed_on: datetime | None
    submited_on: datetime | None
    shipped_on: datetime | None
    accepted_on: datetime | None
    ready_for_quality_control_on: datetime | None
    quality_control_on: datetime | None
    delivered_on: datetime | None
    invoiced_on: datetime | None
    last_invoiced_on: datetime | None
    payment_due_on: datetime | None
    paid_on: datetime | None
    late_fee_on: datetime | None
    cancelled_on: datetime | None
    closed_on: datetime | None
    last_updated_on: datetime | None
    last_updated_by: StrictStr | None
    submited_by_id: StrictInt | None
    sign_off_by_id: StrictInt | None
    vendor_sign_off_by_id: StrictInt | None
    approved_by_id: StrictInt | None
    late_fee_by_id: StrictInt | None
    accepted_by_id: StrictInt | None
    ready_for_quality_control_by_id: StrictInt | None
    quality_control_by_id: StrictInt | None
    created_by_id: StrictInt | None
    completed_by_id: StrictInt | None
    shipped_by_id: StrictInt | None
    delivered_by_id: StrictInt | None
    invoiced_by_id: StrictInt | None
    paid_by_id: StrictInt | None
    cancelled_by_id: StrictInt | None
    closed_by_id: StrictInt | None
    po_number: StrictStr | None
    secondary_po: StrictStr | None
    service_total: StrictFloat | StrictInt | None
    repairs_total: StrictFloat | StrictInt | None
    parts_total: StrictFloat | StrictInt | None
    parts_total_before_discount: StrictFloat | StrictInt | None
    parts_discount_total: StrictFloat | StrictInt | None
    effective_tax_rate: StrictFloat | StrictInt | None
    tax_amount: StrictFloat | StrictInt | None
    shipping_fee: StrictFloat | StrictInt | None
    travel_charge: StrictFloat | StrictInt | None
    late_fee: StrictFloat | StrictInt | None
    is_tax_exempt: StrictBool | None
    service_discount: StrictFloat | StrictInt | None
    trade_in_credit: StrictFloat | StrictInt | None
    prepaid_credit: StrictFloat | StrictInt | None
    grand_total: StrictFloat | StrictInt | None
    paid_amount: StrictFloat | StrictInt | None
    remaining_balance: StrictFloat | StrictInt | None
    service_discount_details: StrictStr | None
    trade_in_credit_details: StrictStr | None
    prepaid_credit_details: StrictStr | None
    payment_notes: StrictStr | None
    service_order_number: StrictInt | None
    legacy_order_number: StrictStr | None
    custom_order_number: StrictStr | None
    payment_status: StrictStr | None
    payment_option: StrictStr | None
    shipment_status: StrictStr | None
    order_status: StrictStr | None
    owner_id: StrictInt | None
    owner_department: StrictStr | None
    client_site: StrictStr | None
    client_site_code: StrictStr | None
    vendor_site: StrictStr | None
    internal: StrictBool | None
    guid: StrictStr | None
    business_from_time: datetime | None
    business_to_time: datetime | None
    site_access_notes: StrictStr | None
    desired_date: datetime | None
    deadline_date: datetime | None
    request_from_date: datetime | None
    request_from_time: datetime | None
    request_to_date: datetime | None
    request_to_time: datetime | None
    order_notes: StrictStr | None
    billing_address: QualerApiModelsAddressToAddressResponseModel | None
    shipping_address: QualerApiModelsAddressToAddressResponseModel | None
    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool
    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(cls, json_str: str) -> QualerApiModelsServiceOrdersToClientOrderResponseModel: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(cls, obj: dict) -> QualerApiModelsServiceOrdersToClientOrderResponseModel: ...

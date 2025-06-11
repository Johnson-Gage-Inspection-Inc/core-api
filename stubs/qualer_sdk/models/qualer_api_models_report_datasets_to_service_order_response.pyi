from datetime import datetime
from pydantic import (
    BaseModel,
    StrictBool as StrictBool,
    StrictFloat as StrictFloat,
    StrictInt as StrictInt,
    StrictStr as StrictStr,
    conbytes as conbytes,
    constr as constr,
)

class QualerApiModelsReportDatasetsToServiceOrderResponse(BaseModel):
    guid: StrictStr | None
    account_number: StrictStr | None
    service_order_number: StrictInt | None
    service_order_number_text: StrictStr | None
    number_of_instruments: StrictInt | None
    parts_discount_total: StrictFloat | StrictInt | None
    po_number: StrictStr | None
    secondary_po: StrictStr | None
    location: StrictStr | None
    shipped_date: datetime | None
    payment_terms: StrictInt | None
    site_access_notes: StrictStr | None
    grace_period: StrictInt | None
    trade_in_credit: StrictFloat | StrictInt | None
    prepaid_credit: StrictFloat | StrictInt | None
    interest_rate: StrictFloat | StrictInt | None
    service_taxation: StrictInt | None
    service_order_id: StrictInt | None
    federal_number: StrictStr | None
    vendor_site_id: StrictInt | None
    vendor_site: StrictStr | None
    site_name: StrictStr | None
    site_code: StrictStr | None
    vendor_name: StrictStr | None
    domain_name: StrictStr | None
    client_company_domain: StrictStr | None
    provider_logo: None | None | None
    client_signature: None | None | None
    vendor_signature: None | None | None
    qr_code: None | None | None
    bar_code: None | None | None
    bar_code_string: StrictStr | None
    po_balance: StrictFloat | StrictInt | None
    service_terms: StrictStr | None
    service_total: StrictFloat | StrictInt | None
    repairs_total: StrictFloat | StrictInt | None
    parts_total: StrictFloat | StrictInt | None
    parts_total_before_discount: StrictFloat | StrictInt | None
    effective_tax_rate: StrictFloat | StrictInt | None
    tax_amount: StrictFloat | StrictInt | None
    shipping_fee: StrictFloat | StrictInt | None
    late_fee: StrictFloat | StrictInt | None
    grand_total: StrictFloat | StrictInt | None
    amount_paid: StrictFloat | StrictInt | None
    balance_total: StrictFloat | StrictInt | None
    travel_charge: StrictFloat | StrictInt | None
    private_notes: StrictStr | None
    service_notes: StrictStr | None
    display_service_comments: StrictBool | None
    display_part_repairs: StrictBool | None
    print_separate_measurement: StrictBool | None
    billing_address1: StrictStr | None
    billing_address2: StrictStr | None
    billing_first_name: StrictStr | None
    billing_last_name: StrictStr | None
    billing_company: StrictStr | None
    billing_country: StrictStr | None
    billing_city: StrictStr | None
    billing_state: StrictStr | None
    billing_zip: StrictStr | None
    billing_phone_number: StrictStr | None
    billing_fax_number: StrictStr | None
    billing_email: StrictStr | None
    shipping_address1: StrictStr | None
    shipping_address2: StrictStr | None
    shipping_first_name: StrictStr | None
    shipping_last_name: StrictStr | None
    shipping_email: StrictStr | None
    shipping_company: StrictStr | None
    shipping_city: StrictStr | None
    shipping_zip: StrictStr | None
    shipping_phone_number: StrictStr | None
    shipping_fax_number: StrictStr | None
    shipping_country: StrictStr | None
    shipping_state: StrictStr | None
    shipping_method: StrictStr | None
    return_shipping_method: StrictStr | None
    tracking_number: StrictStr | None
    provider_billing_address1: StrictStr | None
    provider_billing_address2: StrictStr | None
    provider_billing_first_name: StrictStr | None
    provider_billing_last_name: StrictStr | None
    provider_billing_email: StrictStr | None
    provider_billing_company: StrictStr | None
    provider_billing_city: StrictStr | None
    provider_billing_zip: StrictStr | None
    provider_billing_phone_number: StrictStr | None
    provider_billing_country: StrictStr | None
    provider_billing_state: StrictStr | None
    provider_billing_fax_number: StrictStr | None
    provider_shipping_address1: StrictStr | None
    provider_shipping_address2: StrictStr | None
    provider_shipping_first_name: StrictStr | None
    provider_shipping_last_name: StrictStr | None
    provider_shipping_email: StrictStr | None
    provider_shipping_company: StrictStr | None
    provider_shipping_city: StrictStr | None
    provider_shipping_zip: StrictStr | None
    provider_shipping_phone_number: StrictStr | None
    provider_shipping_country: StrictStr | None
    provider_shipping_state: StrictStr | None
    provider_shipping_fax_number: StrictStr | None
    culture_name: StrictStr | None
    vendor_company_id: StrictInt | None
    client_vendor_id: StrictInt | None
    sign_off_date: datetime | None
    quality_control_date: datetime | None
    client_sign_off_on: datetime | None
    client_sign_off_by_name: StrictStr | None
    client_signed_on: datetime | None
    client_sticker_notes: StrictStr | None
    asset_sticker_notes: StrictStr | None
    order_sticker_notes: StrictStr | None
    quality_control_name: StrictStr | None
    fulfilled_by_name: StrictStr | None
    sign_off_name: StrictStr | None
    display_as_found: StrictBool | None
    display_as_left: StrictBool | None
    created_on: datetime | None
    invoiced_on: datetime | None
    submitted_on: datetime | None
    shipped_on: datetime | None
    completed_on: datetime | None
    accepted_on: datetime | None
    approved_on: datetime | None
    delivered_on: datetime | None
    paid_on: datetime | None
    cancelled_on: datetime | None
    fulfilled_on: datetime | None
    sign_off_on: datetime | None
    vendor_signed_on: datetime | None
    client_notes: StrictStr | None
    order_shipping_option: StrictInt | None
    shipment_status: StrictInt | None
    payment_status: StrictInt | None
    payment_option: StrictStr | None
    order_status: StrictInt | None
    created_by_name: StrictStr | None
    completed_by_name: StrictStr | None
    shipped_by_name: StrictStr | None
    accepted_by_name: StrictStr | None
    approve_by_name: StrictStr | None
    invoiced_by_name: StrictStr | None
    delivered_by_name: StrictStr | None
    paid_by_name: StrictStr | None
    cancelled_by_name: StrictStr | None
    sign_off_by_name: StrictStr | None
    owner_name: StrictStr | None
    owner_department: StrictStr | None
    assignee_name: StrictStr | None
    payment_due_on: datetime | None
    process_date_option: StrictStr | None
    desired_date: datetime | None
    deadline_date: datetime | None
    vendor_sign_off_on: datetime | None
    vendor_sign_off_by_name: StrictStr | None
    service_discount: StrictFloat | StrictInt | None
    return_account: StrictStr | None
    business_hours_from: datetime | None
    business_hours_to: datetime | None
    client_company_alternative_names: StrictStr | None
    client_id: StrictInt | None
    client_class: StrictStr | None
    client_status: StrictStr | None
    client_invoicing: StrictStr | None
    client_standing: StrictStr | None
    client_category: StrictStr | None
    master_template_name: StrictStr | None
    client_site_code: StrictStr | None
    order_workflow_name: StrictStr | None
    request_workflow_name: StrictStr | None
    def provider_logo_validate_regular_expression(cls, value): ...
    def client_signature_validate_regular_expression(cls, value): ...
    def vendor_signature_validate_regular_expression(cls, value): ...
    def qr_code_validate_regular_expression(cls, value): ...
    def bar_code_validate_regular_expression(cls, value): ...
    def process_date_option_validate_enum(cls, value): ...

    class Config:
        allow_population_by_field_name: bool
        validate_assignment: bool

    def to_str(self) -> str: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_json(
        cls, json_str: str
    ) -> QualerApiModelsReportDatasetsToServiceOrderResponse: ...
    def to_dict(self): ...
    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> QualerApiModelsReportDatasetsToServiceOrderResponse: ...

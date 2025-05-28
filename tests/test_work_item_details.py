# tests/test_work_item_details.py
import pytest
from unittest.mock import patch, MagicMock
from deepdiff import DeepDiff

@pytest.fixture
def mock_sdk_calls():
    with patch("routes.work_item_details.make_qualer_client") as mock_make_client, \
         patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api, \
         patch("routes.work_item_details.ClientAssetsApi") as mock_assets_api, \
         patch("routes.work_item_details.ClientAssetAttributesApi") as mock_attr_api, \
         patch("routes.work_item_details.ServiceOrdersApi") as mock_orders_api:

        mock_client = MagicMock()
        mock_make_client.return_value = mock_client        # Mock work item - match expected test data
        mock_work_item = MagicMock()
        mock_work_item.service_order_id = 1171585
        mock_work_item.asset_id = 1270490
        mock_work_item.client_company_id = 57283
        mock_work_item.certificate_number = "56561-067667-01"
        mock_soi_api.return_value.get_work_items_0.return_value = [mock_work_item]

        # Mock asset - match expected test data
        mock_asset = MagicMock()
        mock_asset.asset_name = "Chrome Plus, Oven No. 13, W-CPI-4143, TUS"
        mock_asset.asset_maker = "COL-MET"
        mock_asset.asset_tag = "W-CPI-4143, TUS"
        mock_asset.serial_number = "OVEN NO. 13"
        mock_asset.manufacturer_part_number = "GENERIC 2354"
        mock_asset.category_name = "Thermometer"
        mock_asset.root_category_name = "Thermometers"
        mock_asset.product_manufacturer = "Unidentified"
        mock_asset.product_name = "Thermometers"
        mock_assets_api.return_value.get_asset.return_value = mock_asset

        # Mock attributes
        mock_attr_api.return_value.get_asset_attributes.return_value = {}

        # Mock service order - match expected test data
        mock_order = MagicMock()
        mock_order.po_number = "CHR001150"
        mock_orders_api.return_value.get_work_order.return_value = mock_order

        yield "mocked"
        

def test_work_item_details_success(client, auth_token, mock_sdk_calls):
    assert mock_sdk_calls == "mocked"

    response = client.get(
        "/work-item-details?workItemNumber=56561-067667-01",
        headers={"Authorization": f"Bearer {auth_token}"}
    )

    assert response.status_code == 200
    data = response.get_json()
    expected = {
        'assetAttributes': {},
        'assetId': 1270490,
        'assetMaker': 'COL-MET',
        'assetName': 'Chrome Plus, Oven No. 13, W-CPI-4143, TUS',
        'assetTag': 'W-CPI-4143, TUS',
        'categoryName': 'Thermometer',
        'certificateNumber': '56561-067667-01',
        'clientCompanyId': 57283,
        'manufacturerPartNumber': 'GENERIC 2354',
        'productManufacturer': 'Unidentified',
        'productName': 'Thermometers',
        'purchaseOrderNumber': 'CHR001150',
        'rootCategoryName': 'Thermometers',
        'serialNumber': 'OVEN NO. 13',
        'serviceOrderId': 1171585
    }
    diff = DeepDiff(data, expected, ignore_order=True)
    assert not diff, f"Response data does not match expected: {diff}"

def test_missing_work_item_number(client, auth_token):
    response = client.get(
        "/work-item-details",  # no query param
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    # Flask-Smorest returns 422 for schema validation errors when real auth is enabled
    # When SKIP_AUTH=true, mock returns 400 for consistency with legacy behavior
    expected_status = 422 if auth_token != "fake-token" else 400
    assert response.status_code == expected_status

def test_invalid_work_item_number_format(client, auth_token):
    response = client.get(
        "/work-item-details?workItemNumber=INVALID",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 500
    assert "Invalid work item number format" in response.get_data(as_text=True)

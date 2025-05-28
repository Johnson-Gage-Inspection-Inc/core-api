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
        mock_make_client.return_value = mock_client

        # Mock work item
        mock_work_item = MagicMock()
        mock_work_item.service_order_id = 123456
        mock_work_item.asset_id = 8888
        mock_work_item.client_company_id = 9999
        mock_work_item.certificate_number = "FAKE-000000"
        mock_soi_api.return_value.get_work_items_0.return_value = [mock_work_item]

        # Mock asset
        mock_asset = MagicMock()
        mock_asset.asset_name = "Test Asset"
        mock_asset.asset_maker = "Test Maker"
        mock_asset.asset_tag = "TAG-123"
        mock_asset.serial_number = "SN-001"
        mock_asset.manufacturer_part_number = "MPN-XYZ"
        mock_asset.category_name = "Tools"
        mock_asset.root_category_name = "Equipment"
        mock_asset.product_manufacturer = "Acme"
        mock_asset.product_name = "Caliper"
        mock_assets_api.return_value.get_asset.return_value = mock_asset

        # Mock attributes
        mock_attr_api.return_value.get_asset_attributes.return_value = {}

        # Mock service order
        mock_order = MagicMock()
        mock_order.po_number = "PO-987654"
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
    assert response.status_code == 400
    assert "Missing workItemNumber" in response.get_data(as_text=True)

def test_invalid_work_item_number_format(client, auth_token):
    response = client.get(
        "/work-item-details?workItemNumber=INVALID",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 500
    assert "Invalid work item number format" in response.get_data(as_text=True)

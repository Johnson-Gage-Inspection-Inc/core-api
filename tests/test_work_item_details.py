# tests/test_work_item_details.py
from deepdiff import DeepDiff
from routes.work_item_details import get_work_item_details_for_tus
from unittest.mock import patch, MagicMock
import pytest

SUCCESS_CASES = [
    (
        "56561-067667-01",
        {
            "assetAttributes": {},
            "assetId": 1270490,
            "assetMaker": "COL-MET",
            "assetName": "Chrome Plus, Oven No. 13, W-CPI-4143, TUS",
            "assetTag": "W-CPI-4143, TUS",
            "categoryName": "Thermometer",
            "certificateNumber": "56561-067667-01",
            "clientCompanyId": 57283,
            "manufacturerPartNumber": "GENERIC 2354",
            "productManufacturer": "Unidentified",
            "productName": "Thermometers",
            "purchaseOrderNumber": "CHR001150",
            "rootCategoryName": "Thermometers",
            "serialNumber": "OVEN NO. 13",
            "serviceOrderId": 1171585,
        },
    ),
    (
        "56561-074481-01",
        {
            "assetAttributes": {},
            "assetId": 1270335,
            "assetMaker": "GEHNRICH",
            "assetName": "Capps, Age Oven No. 3, TUS",
            "assetTag": "AGE OVEN NO. 3",
            "categoryName": "Thermometer",
            "certificateNumber": "56561-074481-01",
            "clientCompanyId": 57206,
            "manufacturerPartNumber": "GENERIC 2354",
            "productManufacturer": "Unidentified",
            "productName": "Thermometers",
            "purchaseOrderNumber": "53865",
            "rootCategoryName": "Thermometers",
            "serialNumber": "11108",
            "serviceOrderId": 1259027,
        },
    ),
]

IDS = [number for number, _ in SUCCESS_CASES]

@pytest.mark.parametrize(
    "work_item_number,expected",
    SUCCESS_CASES,
    ids=IDS
)
def test_work_item_details_route_with_auth(client, auth_token, work_item_number, expected):
    resp = client.get(
        f"/work-item-details?workItemNumber={work_item_number}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert resp.status_code == 200
    data = resp.get_json()
    diff = DeepDiff(expected, data, ignore_order=True, report_repetition=True)
    assert diff == {}, f"Differences found:\n{diff}"


def test_work_item_details_route_without_auth(client):
    resp = client.get("/work-item-details?workItemNumber=56561-067667-01")
    assert resp.status_code == 401
    assert resp.text == "Unauthorized"

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

def test_work_item_no_items_found(client, auth_token):
    """Test when no work items are found for the given work item number"""
    import os
    from app import app
    
    # If SKIP_AUTH=true, we need to temporarily restore the real view function
    # to test error conditions, since mock_view_bindings.py overrides them
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None
    
    if skip_auth:
        # Temporarily restore the real view function to test error paths
        from routes.work_item_details import WorkItemDetails
        original_view_func = app.view_functions.get("work-item-details.WorkItemDetails")
        app.view_functions["work-item-details.WorkItemDetails"] = WorkItemDetails().get
    
    try:
        # Patch at the SDK level to return empty list, which should trigger the "no items found" error
        with patch("routes.work_item_details.make_qualer_client") as mock_make_client, \
             patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api:
            
            mock_client = MagicMock()
            mock_make_client.return_value = mock_client
            
            # Return empty list to trigger "No work items found" error
            mock_soi_api.return_value.get_work_items_0.return_value = []
            
            response = client.get(
                "/work-item-details?workItemNumber=56561-067667-01",
                headers={"Authorization": f"Bearer {auth_token}"}
            )
            
            assert response.status_code == 500
            assert "No work items found" in response.get_data(as_text=True)
    finally:
        # Restore the original view function if we changed it
        if skip_auth and original_view_func:
            app.view_functions["work-item-details.WorkItemDetails"] = original_view_func


def test_work_item_multiple_items_found(client, auth_token):
    """Test when multiple work items are found for the given work item number"""
    import os
    from app import app
    
    # If SKIP_AUTH=true, we need to temporarily restore the real view function
    # to test error conditions, since mock_view_bindings.py overrides them
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None
    
    if skip_auth:
        # Temporarily restore the real view function to test error paths
        from routes.work_item_details import WorkItemDetails
        original_view_func = app.view_functions.get("work-item-details.WorkItemDetails")
        app.view_functions["work-item-details.WorkItemDetails"] = WorkItemDetails().get
    
    try:
        # Patch at the SDK level to return multiple items, which should trigger the "multiple items found" error
        with patch("routes.work_item_details.make_qualer_client") as mock_make_client, \
             patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api:
            
            mock_client = MagicMock()
            mock_make_client.return_value = mock_client
            
            # Return multiple items to trigger "Multiple work items found" error
            mock_item1 = MagicMock()
            mock_item2 = MagicMock()
            mock_soi_api.return_value.get_work_items_0.return_value = [mock_item1, mock_item2]
            
            response = client.get(
                "/work-item-details?workItemNumber=56561-067667-01",
                headers={"Authorization": f"Bearer {auth_token}"}
            )
            
            assert response.status_code == 500
            assert "Multiple work items found" in response.get_data(as_text=True)
    finally:
        # Restore the original view function if we changed it
        if skip_auth and original_view_func:
            app.view_functions["work-item-details.WorkItemDetails"] = original_view_func


def test_work_item_missing_required_field(client, auth_token):
    """Test when required fields are missing from work item"""
    import os
    from app import app
    
    # If SKIP_AUTH=true, we need to temporarily restore the real view function
    # to test error conditions, since mock_view_bindings.py overrides them
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None
    
    if skip_auth:
        # Temporarily restore the real view function to test error paths
        from routes.work_item_details import WorkItemDetails
        original_view_func = app.view_functions.get("work-item-details.WorkItemDetails")
        app.view_functions["work-item-details.WorkItemDetails"] = WorkItemDetails().get
    
    try:
        # Patch at the SDK level to return a work item with None values, which should trigger the "missing required field" error
        with patch("routes.work_item_details.make_qualer_client") as mock_make_client, \
             patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api:
            
            mock_client = MagicMock()
            mock_make_client.return_value = mock_client
            
            # Return a work item with None for required fields to trigger error
            mock_item = MagicMock()
            mock_item.service_order_id = None  # This will trigger the missing required field error
            mock_item.asset_id = 12345
            mock_item.client_company_id = 67890
            mock_soi_api.return_value.get_work_items_0.return_value = [mock_item]
            
            response = client.get(
                "/work-item-details?workItemNumber=56561-067667-01",
                headers={"Authorization": f"Bearer {auth_token}"}
            )
            
            assert response.status_code == 500
            assert "Missing required field" in response.get_data(as_text=True)
    finally:
        # Restore the original view function if we changed it
        if skip_auth and original_view_func:
            app.view_functions["work-item-details.WorkItemDetails"] = original_view_func


@patch("routes.work_item_details.make_qualer_client")
@patch("routes.work_item_details.ServiceOrderItemsApi")
@patch("routes.work_item_details.ClientAssetsApi")
@patch("routes.work_item_details.ClientAssetAttributesApi")
@patch("routes.work_item_details.ServiceOrdersApi")
def test_get_work_item_details_for_tus_success(
    mock_orders_api, mock_attr_api, mock_assets_api, mock_soi_api, mock_make_client
):
    mock_client = MagicMock()
    mock_make_client.return_value = mock_client

    work_item = MagicMock()
    work_item.service_order_id = 123
    work_item.asset_id = 456
    work_item.client_company_id = 789
    work_item.certificate_number = "CERT-XYZ"
    mock_soi_api.return_value.get_work_items_0.return_value = [work_item]

    asset = MagicMock()
    asset.asset_name = "Test"
    asset.asset_maker = "Maker"
    asset.asset_tag = "Tag"
    asset.serial_number = "SN"
    asset.manufacturer_part_number = "MPN"
    asset.category_name = "Cat"
    asset.root_category_name = "RootCat"
    asset.product_manufacturer = "ProdMfg"
    asset.product_name = "Prod"
    mock_assets_api.return_value.get_asset.return_value = asset

    mock_attr_api.return_value.get_asset_attributes.return_value = {"calibration_date": "2023-01-01"}

    order = MagicMock()
    order.po_number = "PO123"
    mock_orders_api.return_value.get_work_order.return_value = order

    result = get_work_item_details_for_tus("56561-000001-01")

    assert result["assetId"] == 456
    assert result["certificateNumber"] == "CERT-XYZ"
    assert result["purchaseOrderNumber"] == "PO123"
    assert result["assetAttributes"] == {"calibration_date": "2023-01-01"}

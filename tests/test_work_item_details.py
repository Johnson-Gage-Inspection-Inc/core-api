# tests/test_work_item_details.py
import os
import pytest
from deepdiff import DeepDiff
from routes.work_item_details import get_work_item_details_for_tus
from unittest.mock import patch, MagicMock


# Route-level integration tests with real data
@pytest.mark.parametrize(
    "work_item_number",
    [ "56561-067667-01", "56561-074481-01"],
)
def test_work_item_details_route_success(client, auth_token, work_item_number):
    """Test the route returns expected data structure for valid work items"""
    resp = client.get(
        f"/work-item-details?workItemNumber={work_item_number}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert resp.status_code == 200
    data = resp.get_json()
    keys = ["assetId", "certificateNumber", "assetName", "purchaseOrderNumber"]
    for key in keys:
        assert key in data


def test_work_item_details_route_without_auth(client):
    """Test that unauthenticated requests are rejected"""
    resp = client.get("/work-item-details?workItemNumber=56561-067667-01")
    assert resp.status_code == 401
    assert resp.text == "Unauthorized"


@pytest.mark.parametrize(
    "query_param,expected_status",
    [
        ("", 422),  # Missing parameter
        ("?workItemNumber=INVALID", 500),  # Invalid format
    ],
)
def test_work_item_details_route_validation_errors(client, auth_token, query_param, expected_status):
    """Test route validation for missing or invalid parameters"""
    # Adjust expected status for SKIP_AUTH environment
    if auth_token == "fake-token" and expected_status == 422:
        expected_status = 400
    
    response = client.get(
        f"/work-item-details{query_param}",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == expected_status


# Function-level unit tests with mocks
@pytest.fixture
def mock_apis():
    """Fixture providing mocked API objects"""
    with patch("routes.work_item_details.make_qualer_client") as mock_make_client, \
         patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api, \
         patch("routes.work_item_details.ClientAssetsApi") as mock_assets_api, \
         patch("routes.work_item_details.ClientAssetAttributesApi") as mock_attr_api, \
         patch("routes.work_item_details.ServiceOrdersApi") as mock_orders_api:
        
        mock_client = MagicMock()
        mock_make_client.return_value = mock_client
        
        yield {
            "client": mock_client,
            "soi_api": mock_soi_api,
            "assets_api": mock_assets_api,
            "attr_api": mock_attr_api,
            "orders_api": mock_orders_api,
        }


def _create_mock_work_item(service_order_id=123, asset_id=456, client_company_id=789, cert_number="CERT-123"):
    """Helper to create a mock work item"""
    work_item = MagicMock()
    work_item.service_order_id = service_order_id
    work_item.asset_id = asset_id
    work_item.client_company_id = client_company_id
    work_item.certificate_number = cert_number
    return work_item


def _create_mock_asset():
    """Helper to create a mock asset"""
    asset = MagicMock()
    asset.asset_name = "Test Asset"
    asset.asset_maker = "Test Maker"
    asset.asset_tag = "Test Tag"
    asset.serial_number = "SN123"
    asset.manufacturer_part_number = "MPN123"
    asset.category_name = "Test Category"
    asset.root_category_name = "Root Category"
    asset.product_manufacturer = "Product Manufacturer"
    asset.product_name = "Product Name"
    return asset


def _create_mock_order(po_number="PO123"):
    """Helper to create a mock service order"""
    order = MagicMock()
    order.po_number = po_number
    return order


def test_get_work_item_details_success(mock_apis):
    """Test successful retrieval of work item details"""
    # Setup mocks
    work_item = _create_mock_work_item()
    mock_apis["soi_api"].return_value.get_work_items_0.return_value = [work_item]
    
    asset = _create_mock_asset()
    mock_apis["assets_api"].return_value.get_asset.return_value = asset
    
    mock_apis["attr_api"].return_value.get_asset_attributes.return_value = {"key": "value"}
    
    order = _create_mock_order()
    mock_apis["orders_api"].return_value.get_work_order.return_value = order
    
    # Execute
    result = get_work_item_details_for_tus("56561-000001-01")
    
    # Verify
    assert result["assetId"] == 456
    assert result["certificateNumber"] == "CERT-123"
    assert result["purchaseOrderNumber"] == "PO123"
    assert result["assetAttributes"] == {"key": "value"}


def test_get_work_item_details_auto_prefix(mock_apis):
    """Test that work item numbers are automatically prefixed with '56561-'"""
    # Setup mocks
    work_item = _create_mock_work_item()
    mock_apis["soi_api"].return_value.get_work_items_0.return_value = [work_item]
    
    asset = _create_mock_asset()
    mock_apis["assets_api"].return_value.get_asset.return_value = asset
    
    mock_apis["attr_api"].return_value.get_asset_attributes.return_value = {}
    
    order = _create_mock_order()
    mock_apis["orders_api"].return_value.get_work_order.return_value = order
    
    # Execute with unprefixed work item number
    get_work_item_details_for_tus("000001-01")
    
    # Verify the API was called with the prefixed version
    mock_apis["soi_api"].return_value.get_work_items_0.assert_called_with(work_item_number="56561-000001-01")


@pytest.mark.parametrize(
    "work_items,expected_error",
    [
        ([], "No work items found"),
        ([_create_mock_work_item(), _create_mock_work_item()], "Multiple work items found"),
        ([_create_mock_work_item(service_order_id=None)], "Missing required field"),
    ],
)
def test_get_work_item_details_error_conditions(mock_apis, work_items, expected_error):
    """Test various error conditions in work item retrieval"""
    mock_apis["soi_api"].return_value.get_work_items_0.return_value = work_items
    
    with pytest.raises(ValueError, match=expected_error):
        get_work_item_details_for_tus("56561-000001-01")

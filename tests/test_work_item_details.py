# tests/test_work_item_details.py
import os
from typing import Any, Dict, Generator, List
from unittest.mock import MagicMock, patch

import pytest
from flask.testing import FlaskClient

from routes.work_item_details import get_work_item_details_for_tus
from utils.schemas import WorkItemNumber


# Route-level integration tests with real data
@pytest.mark.skipif(
    os.getenv("SKIP_AUTH", "false").lower() == "false",
    reason="Skipping work-item-details test when SKIP_AUTH=false due to external API issues",
)
@pytest.mark.parametrize(
    "work_item_number",
    ["56561-067667-01", "56561-074481-01"],
)
def test_work_item_details_route_success(
    client: FlaskClient, auth_token: str, work_item_number: str
) -> None:
    """Test the route returns expected data structure for valid work items"""
    resp = client.get(
        f"/work-item-details?workItemNumber={work_item_number}",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert resp.status_code == 200
    data = resp.get_json()
    keys = ["assetId", "certificateNumber", "assetName", "purchaseOrderNumber"]
    for key in keys:
        assert key in data


def test_work_item_details_route_without_auth(client: FlaskClient) -> None:
    """Test that unauthenticated requests are rejected"""
    resp = client.get("/work-item-details?workItemNumber=56561-067667-01")
    assert resp.status_code == 401
    # Support both simple text and JSON format for Unauthorized message
    assert "Unauthorized" in resp.text


@pytest.mark.parametrize(
    "query_param,expected_status",
    [
        ("", 422),  # Missing parameter
        ("?workItemNumber=INVALID", 500),  # Invalid format
    ],
)
def test_work_item_details_route_validation_errors(
    client: FlaskClient, auth_token: str, query_param: str, expected_status: int
) -> None:
    """Test route validation for missing or invalid parameters"""
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"

    # Adjust expected status for SKIP_AUTH environment
    if skip_auth:
        if query_param == "":
            expected_status = 400  # Missing param becomes 400 in mock mode
        elif "INVALID" in query_param:
            # In SKIP_AUTH=true mode, our mock doesn't trigger the 500 error for INVALID
            # so we'll skip this assertion
            pytest.skip("Mock doesn't validate work item number format")

    response = client.get(
        f"/work-item-details{query_param}",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == expected_status


# Function-level unit tests with mocks
@pytest.fixture
def mock_apis() -> Generator[Dict[str, Any], None, None]:
    """Fixture providing mocked API objects"""
    with (
        patch("routes.work_item_details.make_qualer_client") as mock_make_client,
        patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api,
        patch("routes.work_item_details.ClientAssetsApi") as mock_assets_api,
        patch("routes.work_item_details.ClientAssetAttributesApi") as mock_attr_api,
        patch("routes.work_item_details.ServiceOrdersApi") as mock_orders_api,
    ):

        mock_client = MagicMock()
        mock_make_client.return_value = mock_client

        yield {
            "client": mock_client,
            "soi_api": mock_soi_api,
            "assets_api": mock_assets_api,
            "attr_api": mock_attr_api,
            "orders_api": mock_orders_api,
        }


def _create_mock_work_item(
    service_order_id: int = 123,
    asset_id: int = 456,
    client_company_id: int = 789,
    cert_number: str = "CERT-123",
) -> MagicMock:
    """Helper to create a mock work item"""
    work_item = MagicMock()
    work_item.service_order_id = service_order_id
    work_item.asset_id = asset_id
    work_item.client_company_id = client_company_id
    work_item.certificate_number = cert_number
    return work_item


def _create_mock_asset() -> MagicMock:
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


def _create_mock_order(po_number: str = "PO123") -> MagicMock:
    """Helper to create a mock service order"""
    order = MagicMock()
    order.po_number = po_number
    return order


def test_get_work_item_details_success(mock_apis: Dict[str, Any]) -> None:
    """Test successful retrieval of work item details"""
    # Setup mocks
    work_item = _create_mock_work_item()
    mock_apis["soi_api"].return_value.get_work_items_0.return_value = [work_item]

    asset = _create_mock_asset()
    mock_apis["assets_api"].return_value.get_asset_get2.return_value = asset

    mock_apis["attr_api"].return_value.get_asset_attributes_get2.return_value = {
        "key": "value"
    }

    order = _create_mock_order()
    mock_apis["orders_api"].return_value.get_work_order.return_value = order

    # Execute
    wo_number = WorkItemNumber("56561-000001-01")
    result = get_work_item_details_for_tus(wo_number)

    # Verify
    assert result["assetId"] == 456
    assert result["certificateNumber"] == "CERT-123"
    assert result["purchaseOrderNumber"] == "PO123"
    assert result["assetAttributes"] == {"key": "value"}


def test_get_work_item_details_auto_prefix(mock_apis: Dict[str, Any]) -> None:
    """Test that work item numbers are automatically prefixed with '56561-'"""
    # Setup mocks
    work_item = _create_mock_work_item()
    mock_apis["soi_api"].return_value.get_work_items.return_value = [work_item]

    asset = _create_mock_asset()
    mock_apis["assets_api"].return_value.get_asset_get2.return_value = asset

    mock_apis["attr_api"].return_value.get_asset_attributes_get2.return_value = {}

    order = _create_mock_order()
    mock_apis["orders_api"].return_value.get_work_order.return_value = order

    # Execute with unprefixed work item number
    wo_number = WorkItemNumber("000001-01")
    get_work_item_details_for_tus(wo_number)

    # Verify the API was called with the prefixed version
    mock_apis["soi_api"].return_value.get_work_items_0.assert_called_with(
        work_item_number=WorkItemNumber("56561-000001-01")
    )


@pytest.mark.parametrize(
    "work_items,expected_error",
    [
        ([], "No work items found"),
        (
            [_create_mock_work_item(), _create_mock_work_item()],
            "Multiple work items found",
        ),
        ([_create_mock_work_item(service_order_id=None)], "Missing required field"),
    ],
)
def test_get_work_item_details_error_conditions(
    mock_apis: Dict[str, Any], work_items: List[MagicMock], expected_error: str
) -> None:
    """Test various error conditions in work item retrieval"""
    mock_apis["soi_api"].return_value.get_work_items_0.return_value = work_items

    with pytest.raises(ValueError, match=expected_error):
        wo_number = WorkItemNumber("56561-000001-01")
        get_work_item_details_for_tus(wo_number)


def test_work_item_details_sdk_validation_error(
    client: FlaskClient, auth_token: str
) -> None:
    """Test that SDK validation errors are handled gracefully"""
    import os

    from app import app

    # If SKIP_AUTH=true, temporarily restore real view function to test error handling
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None

    if skip_auth:
        from routes.work_item_details import WorkItemDetails

        original_view_func = app.view_functions.get("work-item-details.WorkItemDetails")
        app.view_functions["work-item-details.WorkItemDetails"] = WorkItemDetails().get

    try:
        with patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api:
            # Simulate SDK validation error for asset_status field
            mock_soi_api.return_value.get_work_items_0.side_effect = ValueError(
                "Invalid value for `asset_status` (Active), must be one of ['0', '1', '2', '3', '4']"
            )

            response = client.get(
                "/work-item-details?workItemNumber=56561-067667-02",
                headers={"Authorization": f"Bearer {auth_token}"},
            )

            assert response.status_code == 500
            data = response.get_json()
            assert "Asset data format error from Qualer API" in data["message"]
            assert "SDK update" in data["message"]
    finally:
        if skip_auth and original_view_func:
            app.view_functions["work-item-details.WorkItemDetails"] = original_view_func


def test_work_item_details_generic_validation_error(
    client: FlaskClient, auth_token: str
) -> None:
    """Test that other SDK validation errors are handled with details"""
    import os

    from app import app

    # If SKIP_AUTH=true, temporarily restore real view function to test error handling
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None

    if skip_auth:
        from routes.work_item_details import WorkItemDetails

        original_view_func = app.view_functions.get("work-item-details.WorkItemDetails")
        app.view_functions["work-item-details.WorkItemDetails"] = WorkItemDetails().get

    try:
        with patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api:
            # Simulate different SDK validation error
            mock_soi_api.return_value.get_work_items_0.side_effect = ValueError(
                "Invalid value for `category_status` (Inactive), must be one of ['active', 'inactive']"
            )

            response = client.get(
                "/work-item-details?workItemNumber=56561-067667-02",
                headers={"Authorization": f"Bearer {auth_token}"},
            )

            assert response.status_code == 500
            data = response.get_json()
            assert "Data validation error from Qualer API" in data["message"]
            assert "must be one of" in data["message"]
    finally:
        if skip_auth and original_view_func:
            app.view_functions["work-item-details.WorkItemDetails"] = original_view_func


def test_work_item_details_asset_api_validation_error(
    client: FlaskClient, auth_token: str
) -> None:
    """Test that SDK validation errors from ClientAssetsApi are handled gracefully"""
    import os

    from app import app

    # If SKIP_AUTH=true, temporarily restore real view function to test error handling
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None

    if skip_auth:
        from routes.work_item_details import WorkItemDetails

        original_view_func = app.view_functions.get("work-item-details.WorkItemDetails")
        app.view_functions["work-item-details.WorkItemDetails"] = WorkItemDetails().get

    try:
        with (
            patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api,
            patch("routes.work_item_details.ClientAssetsApi") as mock_assets_api,
        ):

            # Mock successful work item retrieval
            work_item = _create_mock_work_item()
            mock_soi_api.return_value.get_work_items_0.return_value = [work_item]

            # Simulate SDK validation error when getting asset details
            mock_assets_api.return_value.get_asset_get2.side_effect = ValueError(
                "Invalid value for `asset_status` (Active), must be one of ['0', '1', '2', '3', '4']"
            )

            response = client.get(
                "/work-item-details?workItemNumber=56561-067667-02",
                headers={"Authorization": f"Bearer {auth_token}"},
            )

            assert response.status_code == 500
            data = response.get_json()
            assert "Asset data format error from Qualer API" in data["message"]
            assert "SDK update" in data["message"]
    finally:
        if skip_auth and original_view_func:
            app.view_functions["work-item-details.WorkItemDetails"] = original_view_func


def test_work_item_details_service_order_api_validation_error(
    client: FlaskClient, auth_token: str
) -> None:
    """Test that SDK validation errors from ServiceOrdersApi are handled gracefully"""
    import os

    from app import app

    # If SKIP_AUTH=true, temporarily restore real view function to test error handling
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None

    if skip_auth:
        from routes.work_item_details import WorkItemDetails

        original_view_func = app.view_functions.get("work-item-details.WorkItemDetails")
        app.view_functions["work-item-details.WorkItemDetails"] = WorkItemDetails().get

    try:
        with (
            patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api,
            patch("routes.work_item_details.ClientAssetsApi") as mock_assets_api,
            patch("routes.work_item_details.ServiceOrdersApi") as mock_orders_api,
            patch("routes.work_item_details.ClientAssetAttributesApi") as mock_attr_api,
        ):

            # Mock successful work item and asset retrieval
            work_item = _create_mock_work_item()
            mock_soi_api.return_value.get_work_items_0.return_value = [work_item]

            asset = _create_mock_asset()
            mock_assets_api.return_value.get_asset_get2.return_value = asset

            mock_attr_api.return_value.get_asset_attributes_get2.return_value = {}

            # Simulate SDK validation error when getting service order details
            mock_orders_api.return_value.get_work_order.side_effect = ValueError(
                "Invalid value for `asset_status` (PENDING), must be one of ['ACTIVE', 'INACTIVE', 'RETIRED']"
            )

            response = client.get(
                "/work-item-details?workItemNumber=56561-067667-02",
                headers={"Authorization": f"Bearer {auth_token}"},
            )

            assert response.status_code == 500
            data = response.get_json()
            assert "Asset data format error from Qualer API" in data["message"]
            assert "SDK update" in data["message"]
    finally:
        if skip_auth and original_view_func:
            app.view_functions["work-item-details.WorkItemDetails"] = original_view_func


def test_work_item_details_asset_attributes_api_validation_error(
    client: FlaskClient, auth_token: str
) -> None:
    """Test that SDK validation errors from ClientAssetAttributesApi are handled gracefully"""
    import os

    from app import app

    # If SKIP_AUTH=true, temporarily restore real view function to test error handling
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None

    if skip_auth:
        from routes.work_item_details import WorkItemDetails

        original_view_func = app.view_functions.get("work-item-details.WorkItemDetails")
        app.view_functions["work-item-details.WorkItemDetails"] = WorkItemDetails().get

    try:
        with (
            patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api,
            patch("routes.work_item_details.ClientAssetsApi") as mock_assets_api,
            patch("routes.work_item_details.ServiceOrdersApi") as mock_orders_api,
            patch("routes.work_item_details.ClientAssetAttributesApi") as mock_attr_api,
        ):  # Mock successful work item, asset, and service order retrieval
            work_item = _create_mock_work_item()
            mock_soi_api.return_value.get_work_items_0.return_value = [work_item]

            asset = _create_mock_asset()
            mock_assets_api.return_value.get_asset_get2.return_value = asset

            order = _create_mock_order()
            mock_orders_api.return_value.get_work_order.return_value = order

            # Simulate SDK validation error when getting asset attributes
            mock_attr_api.return_value.get_asset_attributes_get2.side_effect = ValueError(
                "Invalid value for `asset_status` (2), must be one of ['0', '1', '3', '4', '5']"
            )

            response = client.get(
                "/work-item-details?workItemNumber=56561-067667-02",
                headers={"Authorization": f"Bearer {auth_token}"},
            )

            assert response.status_code == 500
            data = response.get_json()
            assert "Asset data format error from Qualer API" in data["message"]
            assert "SDK update" in data["message"]
    finally:
        if skip_auth and original_view_func:
            app.view_functions["work-item-details.WorkItemDetails"] = original_view_func


def test_work_item_details_comprehensive_validation_scenarios(
    client: FlaskClient, auth_token: str
) -> None:
    """Test various realistic SDK validation error scenarios that could occur in production"""
    import os

    from app import app

    # If SKIP_AUTH=true, temporarily restore real view function to test error handling
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None

    if skip_auth:
        from routes.work_item_details import WorkItemDetails

        original_view_func = app.view_functions.get("work-item-details.WorkItemDetails")
        app.view_functions["work-item-details.WorkItemDetails"] = WorkItemDetails().get

    # Test different validation error scenarios
    test_cases = [
        {
            "error": "Invalid value for `asset_status` (Active), must be one of ['0', '1', '2', '3', '4']",
            "expected_message": "Asset data format error from Qualer API",
        },
        {
            "error": "Invalid value for `asset_status` (2), must be one of ['0', '1', '3', '4', '5']",
            "expected_message": "Asset data format error from Qualer API",
        },
        {
            "error": "Invalid value for `asset_status` (PENDING), must be one of ['ACTIVE', 'INACTIVE']",
            "expected_message": "Asset data format error from Qualer API",
        },
        {
            "error": "Invalid value for `category_status` (Inactive), must be one of ['active', 'inactive']",
            "expected_message": "Data validation error from Qualer API",
        },
    ]

    try:
        for i, test_case in enumerate(test_cases):
            with patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api:
                # Simulate the validation error
                mock_soi_api.return_value.get_work_items_0.side_effect = ValueError(
                    test_case["error"]
                )

                response = client.get(
                    f"/work-item-details?workItemNumber=56561-067667-{i:02d}",
                    headers={"Authorization": f"Bearer {auth_token}"},
                )

                assert response.status_code == 500
                data = response.get_json()
                assert test_case["expected_message"] in data["message"]
    finally:
        if skip_auth and original_view_func:
            app.view_functions["work-item-details.WorkItemDetails"] = original_view_func


def test_work_item_details_threadpool_validation_error(
    client: FlaskClient, auth_token: str
) -> None:
    """Test SDK validation errors that occur during ThreadPoolExecutor execution"""
    import os

    from app import app

    # If SKIP_AUTH=true, temporarily restore real view function to test error handling
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None

    if skip_auth:
        from routes.work_item_details import WorkItemDetails

        original_view_func = app.view_functions.get("work-item-details.WorkItemDetails")
        app.view_functions["work-item-details.WorkItemDetails"] = WorkItemDetails().get

    try:
        with (
            patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api,
            patch("routes.work_item_details.ClientAssetsApi") as mock_assets_api,
            patch("routes.work_item_details.ServiceOrdersApi") as mock_orders_api,
            patch("routes.work_item_details.ClientAssetAttributesApi") as mock_attr_api,
        ):

            # Mock successful work item retrieval
            work_item = _create_mock_work_item()
            mock_soi_api.return_value.get_work_items_0.return_value = [work_item]

            # Mock successful asset and order retrieval
            asset = _create_mock_asset()
            mock_assets_api.return_value.get_asset_get2.return_value = asset

            order = _create_mock_order()
            mock_orders_api.return_value.get_work_order.return_value = order

            # Mock asset attributes API to raise the validation error that bubbles up
            mock_attr_api.return_value.get_asset_attributes_get2.side_effect = ValueError(
                "Invalid value for `asset_status` (Active), must be one of ['0', '1', '2', '3', '4']"
            )

            response = client.get(
                "/work-item-details?workItemNumber=56561-067667-02",
                headers={"Authorization": f"Bearer {auth_token}"},
            )

            assert response.status_code == 500
            data = response.get_json()
            assert "Asset data format error from Qualer API" in data["message"]
            assert "SDK update" in data["message"]
    finally:
        if skip_auth and original_view_func:
            app.view_functions["work-item-details.WorkItemDetails"] = original_view_func


def test_work_item_details_realistic_production_errors(
    client: FlaskClient, auth_token: str
) -> None:
    """Test realistic production scenarios where asset status values from Qualer don't match SDK expectations"""
    import os

    from app import app

    # If SKIP_AUTH=true, temporarily restore real view function to test error handling
    skip_auth = os.getenv("SKIP_AUTH", "false").lower() == "true"
    original_view_func = None

    if skip_auth:
        from routes.work_item_details import WorkItemDetails

        original_view_func = app.view_functions.get("work-item-details.WorkItemDetails")
        app.view_functions["work-item-details.WorkItemDetails"] = WorkItemDetails().get

    # Test cases based on realistic scenarios where Qualer API format changes
    production_scenarios = [
        {
            "error": "Invalid value for `asset_status` (Active), must be one of ['0', '1', '2', '3', '4']",
            "description": "String status vs numeric expected",
            "api": "assets",
        },
        {
            "error": "Invalid value for `asset_status` (5), must be one of ['0', '1', '2', '3', '4']",
            "description": "New numeric status value added",
            "api": "assets",
        },
        {
            "error": "Invalid value for `asset_status` (RETIRED), must be one of ['ACTIVE', 'INACTIVE']",
            "description": "New enum value added",
            "api": "service_orders",
        },
        {
            "error": "Invalid value for `asset_status` (null), must be one of ['0', '1', '2', '3', '4']",
            "description": "Null value handling",
            "api": "attributes",
        },
    ]

    try:
        for i, scenario in enumerate(production_scenarios):
            with patch("routes.work_item_details.ServiceOrderItemsApi") as mock_soi_api:
                # Mock successful work item retrieval
                work_item = _create_mock_work_item()
                mock_soi_api.return_value.get_work_items_0.return_value = [work_item]

                # Simulate the validation error based on the scenario API
                if scenario["api"] == "assets":
                    with patch(
                        "routes.work_item_details.ClientAssetsApi"
                    ) as mock_assets_api:
                        mock_assets_api.return_value.get_asset_get2.side_effect = ValueError(
                            scenario["error"]
                        )

                        response = client.get(
                            f"/work-item-details?workItemNumber=56561-067667-{i:02d}",
                            headers={"Authorization": f"Bearer {auth_token}"},
                        )
                elif scenario["api"] == "service_orders":
                    with (
                        patch(
                            "routes.work_item_details.ClientAssetsApi"
                        ) as mock_assets_api,
                        patch(
                            "routes.work_item_details.ServiceOrdersApi"
                        ) as mock_orders_api,
                        patch(
                            "routes.work_item_details.ClientAssetAttributesApi"
                        ) as mock_attr_api,
                    ):

                        # Mock successful asset and attributes
                        asset = _create_mock_asset()
                        mock_assets_api.return_value.get_asset_get2.return_value = asset
                        mock_attr_api.return_value.get_asset_attributes_get2.return_value = (
                            {}
                        )

                        # Error in service order API
                        mock_orders_api.return_value.get_work_order.side_effect = (
                            ValueError(scenario["error"])
                        )

                        response = client.get(
                            f"/work-item-details?workItemNumber=56561-067667-{i:02d}",
                            headers={"Authorization": f"Bearer {auth_token}"},
                        )
                elif scenario["api"] == "attributes":
                    with (
                        patch(
                            "routes.work_item_details.ClientAssetsApi"
                        ) as mock_assets_api,
                        patch(
                            "routes.work_item_details.ServiceOrdersApi"
                        ) as mock_orders_api,
                        patch(
                            "routes.work_item_details.ClientAssetAttributesApi"
                        ) as mock_attr_api,
                    ):

                        # Mock successful asset and service order
                        asset = _create_mock_asset()
                        mock_assets_api.return_value.get_asset_get2.return_value = asset
                        order = _create_mock_order()
                        mock_orders_api.return_value.get_work_order.return_value = order

                        # Error in attributes API
                        mock_attr_api.return_value.get_asset_attributes_get2.side_effect = (
                            ValueError(scenario["error"])
                        )

                        response = client.get(
                            f"/work-item-details?workItemNumber=56561-067667-{i:02d}",
                            headers={"Authorization": f"Bearer {auth_token}"},
                        )

                # All should return the specific asset status error message
                assert response.status_code == 500
                data = response.get_json()
                assert "Asset data format error from Qualer API" in data["message"]
                assert "SDK update" in data["message"]

    finally:
        if skip_auth and original_view_func:
            app.view_functions["work-item-details.WorkItemDetails"] = original_view_func

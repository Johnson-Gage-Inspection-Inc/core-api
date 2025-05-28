import pytest
from unittest.mock import patch, MagicMock
from routes.work_item_details import get_work_item_details_for_tus

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

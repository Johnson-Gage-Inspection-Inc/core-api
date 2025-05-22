# routes/work_item_details.py
from concurrent.futures import ThreadPoolExecutor
from flask import Blueprint, request, jsonify
from utils.auth import require_auth
from qualer_sdk import (
    ServiceOrdersApi,
    ServiceOrderItemsApi,
    ApiClient,
    Configuration,
    ClientAssetsApi,
    ClientAssetAttributesApi)

bp = Blueprint("main", __name__)


@bp.route("/work_item_details", methods=["GET"])
@require_auth
def work_item_details_route():
    """Fetches work item details for a given work item number."""
    
    def get_work_item_details_for_tus(work_item_number):
        """
        Fetches work item details for a given work item number.
        
        Args:
            work_item_number (str): The work item number to fetch details for.
            
        Returns:
            list: A dictionary containing work item details.
        """
        from os import getenv
        import re

        pattern = r"^(56561-)?\d{6}(\.\d{2})?(-\d{2})(R\d{1,2})?$"
        if not re.match(pattern, work_item_number):
            raise ValueError("Invalid work item number format.")

        config = Configuration()
        config.host = "https://jgiquality.qualer.com"

        client = ApiClient(configuration=config)
        bearer_token = f'Api-Token {getenv("QUALER_API_KEY")}'
        client.default_headers["Authorization"] = bearer_token

        soi_api = ServiceOrderItemsApi(client)
        work_items = soi_api.get_work_items_0(
            work_item_number=work_item_number
        )
        if len(work_items) == 0:
            raise ValueError(
                "No work items found for the given work item number."
                )
        if len(work_items) > 1:
            raise ValueError(
                "Multiple work items found for the given work item number."
                )
        # Assuming we only need the first work item
        item = work_items[0]

        service_order_id = item.service_order_id
        asset_id = item.asset_id
        client_company_id = item.client_company_id

        for field in [service_order_id, asset_id, client_company_id]:
            if field is None:
                raise ValueError(f"Missing required field: {field}")

        # Fetch the client asset, attributes, and service order in parallel
        with ThreadPoolExecutor() as executor:
            future_client_asset = executor.submit(
                ClientAssetsApi(client).get_asset,
                asset_id=asset_id
            )
            future_attributes = executor.submit(
                ClientAssetAttributesApi(client).get_asset_attributes,
                asset_id=asset_id
            )
            future_service_order = executor.submit(
                ServiceOrdersApi(client).get_work_order,
                service_order_id=service_order_id
            )

            client_asset = future_client_asset.result()
            client_asset_attributes = future_attributes.result()
            service_order = future_service_order.result()

        # Assemble the response
        return {
            "clientCompanyId": client_company_id,
            "serviceOrderId": service_order_id,
            "assetId": asset_id,
            "certificateNumber": item.certificate_number,
            "assetName": client_asset.asset_name,
            "assetMaker": client_asset.asset_maker,
            "assetTag": client_asset.asset_tag,
            "serialNumber": client_asset.serial_number,
            "manufacturerPartNumber": client_asset.manufacturer_part_number,
            "categoryName": client_asset.category_name,
            "rootCategoryName": client_asset.root_category_name,
            "productManufacturer": client_asset.product_manufacturer,
            "productName": client_asset.product_name,
            "purchaseOrderNumber": service_order.po_number,
            "assetAttributes": client_asset_attributes
        }

    work_item_number = request.args.get("workItemNumber")
    if not work_item_number:
        return jsonify({"error": "Missing workItemNumber"}), 400

    try:
        details = get_work_item_details_for_tus(work_item_number)
        return jsonify(details)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
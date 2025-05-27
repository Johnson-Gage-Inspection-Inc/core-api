# routes/work_item_details.py
from concurrent.futures import ThreadPoolExecutor
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import WorkItemDetailsSchema, WorkItemDetailsQuerySchema
from utils.auth import require_auth
import re
from utils.qualer_client import make_qualer_client
from qualer_sdk import (
    ServiceOrdersApi,
    ServiceOrderItemsApi,
    ClientAssetsApi,
    ClientAssetAttributesApi)

blp = Blueprint("work_item_details", __name__, url_prefix="/")


def get_work_item_details_for_tus(item_no):
    pattern = r"^(56561-)?\d{6}(\.\d{2})?(-\d{2})(R\d{1,2})?$"
    if not re.match(pattern, item_no):
        raise ValueError("Invalid work item number format.")

    client = make_qualer_client()

    soi_api = ServiceOrderItemsApi(client)
    work_items = soi_api.get_work_items_0(work_item_number=item_no)

    if len(work_items) == 0:
        raise ValueError(
            "No work items found for the given work item number."
            )
    if len(work_items) > 1:
        raise ValueError(
            "Multiple work items found for the given work item number."
            )

    item = work_items[0]
    service_order_id = item.service_order_id
    asset_id = item.asset_id
    client_company_id = item.client_company_id

    for field in [service_order_id, asset_id, client_company_id]:
        if field is None:
            raise ValueError(f"Missing required field: {field}")

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

@blp.route("/work_item_details")
class WorkItemDetails(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}])
    @blp.arguments(WorkItemDetailsQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, WorkItemDetailsSchema)
    def get(self, workItemNumber):
        if not workItemNumber:
            abort(400, message="Missing workItemNumber")

        try:
            return get_work_item_details_for_tus(workItemNumber)
        except Exception as e:
            abort(500, message=str(e))

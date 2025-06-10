# routes/work_item_details.py
import re
from concurrent.futures import ThreadPoolExecutor

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from qualer_sdk import (
    ClientAssetAttributesApi,
    ClientAssetsApi,
    ServiceOrderItemsApi,
    ServiceOrdersApi,
)

from utils.auth import require_auth
from utils.qualer_client import make_qualer_client
from utils.schemas import (
    WorkItemDetailsQuerySchema,
    WorkItemDetailsSchema,
    WorkItemNumber,
)

blp = Blueprint("work-item-details", __name__, url_prefix="/")


def get_work_item_details_for_tus(item_no: WorkItemNumber):

    client = make_qualer_client()

    soi_api = ServiceOrderItemsApi(client)
    work_items = soi_api.get_work_items_0(work_item_number=item_no)

    if len(work_items) == 0:
        raise ValueError("No work items found for the given work item number.")
    if len(work_items) > 1:
        raise ValueError("Multiple work items found for the given work item number.")

    item = work_items[0]
    service_order_id = item.service_order_id
    asset_id = item.asset_id
    client_company_id = item.client_company_id

    for field in [service_order_id, asset_id, client_company_id]:
        if field is None:
            raise ValueError(f"Missing required field: {field}")

    with ThreadPoolExecutor() as executor:
        future_client_asset = executor.submit(
            ClientAssetsApi(client).get_asset, asset_id=asset_id
        )
        future_attributes = executor.submit(
            ClientAssetAttributesApi(client).get_asset_attributes, asset_id=asset_id
        )
        future_service_order = executor.submit(
            ServiceOrdersApi(client).get_work_order, service_order_id=service_order_id
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
        "assetAttributes": client_asset_attributes,
    }


@blp.route("/work-item-details")
class WorkItemDetails(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Pyro"])
    @blp.arguments(WorkItemDetailsQuerySchema, location="query", as_kwargs=True)
    @blp.response(200, WorkItemDetailsSchema)
    def get(self, workItemNumber: WorkItemNumber) -> dict:
        """
        Get detailed TUS (Testing, Upgrading, Servicing) information for a work item.

        This endpoint retrieves comprehensive details about a work item by its number,
        including asset information, service order details, and attributes. The work
        item number must follow a specific format pattern for validation.

        **Args**:
        - workItemNumber (WorkItemNumber): The work item number to look up. Must match pattern:
                r"^(56561-)?\\d{6}(\\.\\d{2})?(-\\d{2})(R\\d{1,2})?$"
                Examples: "123456-01", "56561-123456.01-02", "123456.01-02R1"

        **Returns**:
        - **dict**: Comprehensive work item details containing:
          - clientCompanyId: ID of the client company
          - serviceOrderId: ID of the associated service order
          - assetId: ID of the asset being serviced
          - certificateNumber: Certificate number for the work item
          - assetName: Name of the asset
          - assetMaker: Manufacturer of the asset
          - assetTag: Asset tag identifier
          - serialNumber: Serial number of the asset
          - manufacturerPartNumber: Manufacturer's part number
          - categoryName: Asset category name
          - rootCategoryName: Root category name
          - productManufacturer: Product manufacturer
          - productName: Product name
          - purchaseOrderNumber: Associated purchase order number
          - assetAttributes: List of asset attributes and their values

        **Raises**:
        - **400**: If workItemNumber parameter is missing
        - **401**: If authentication token is invalid or missing
        - **422**: If workItemNumber format is invalid
        - **500**: If work item not found, multiple work items found, missing required fields, or API communication error

        **Example**: GET /work-item-details?workItemNumber=123456-01 with Authorization: Bearer <token>

        **Response**: Object with clientCompanyId, serviceOrderId, assetId, certificateNumber, assetName, assetMaker, assetTag, serialNumber, manufacturerPartNumber, categoryName, rootCategoryName, productManufacturer, productName, purchaseOrderNumber, and assetAttributes
        """
        if not workItemNumber:
            abort(400, message="Missing workItemNumber")

        try:
            return get_work_item_details_for_tus(workItemNumber)
        except ValueError as e:
            # Handle specific validation errors with user-friendly messages
            error_msg = str(e)
            if "Invalid value for `asset_status`" in error_msg:
                abort(
                    500,
                    message="Asset data format error from Qualer API. The asset status format has changed and requires SDK update.",
                )
            elif "must be one of" in error_msg:
                abort(
                    500, message=f"Data validation error from Qualer API: {error_msg}"
                )
            else:
                abort(500, message=str(e))
        except Exception as e:
            abort(500, message=str(e))

# routes/asset_service_records.py
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields
from qualer_sdk import AssetServiceRecordsApi

from utils.auth import require_auth
from utils.qualer_client import make_qualer_client
from utils.schemas import AssetServiceRecordResponseSchema

blp = Blueprint("asset-service-records", __name__, url_prefix="/")


class AssetServiceRecordQuerySchema(Schema):
    assetId = fields.Str(
        required=True,
        metadata={"description": "The ID of the asset to retrieve service records for"},
    )


@blp.route("/asset-service-records/<assetId>")
class AssetServiceRecord(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Qualer"])
    @blp.response(200, AssetServiceRecordResponseSchema(many=True))
    def get(self, assetId):
        """
        Retrieve all asset service records for a specific asset from Qualer.

        This endpoint fetches all asset service records associated with a given asset ID
        from the Qualer system. The response includes a list of service records with
        comprehensive details about each service performed on the asset.

        **Parameters**:
        - **assetId** (str): The unique identifier of the asset to retrieve service records for

        **Returns**:
        - **list**: An array of asset service record objects, each containing:
          - AssetServiceRecordId: Unique identifier of the service record
          - AssetId: ID of the associated asset
          - ServiceDate: Date when the service was performed
          - ResultStatus: Status of the service result
          - SerialNumber: Serial number of the serviced asset
          - AssetName: Name of the serviced asset
          - ServiceType: Type of service performed
          - Additional service record attributes as defined by Qualer API

        **Raises**:
        - **400**: If assetId parameter is missing or invalid
        - **401**: If authentication token is invalid or missing
        - **404**: If asset with the specified ID is not found or has no service records
        - **500**: If there's an error communicating with the Qualer API

        **Example**: GET /asset-service-records/12345 with Authorization: Bearer <token>

        **Response**: Array of asset service record objects for the specified asset
        """
        if not assetId:
            abort(400, message="Missing assetId")

        try:
            client = make_qualer_client()
            api = AssetServiceRecordsApi(client)
            return api.get_asset_service_records_by_asset(asset_id=assetId)
        except Exception as e:
            # Check if it's a 404 error (asset not found)
            if hasattr(e, "status") and e.status == 404:
                abort(
                    404,
                    message=f"Asset with ID '{assetId}' not found or has no service records",
                )
            else:
                abort(500, message=f"Error fetching asset service records: {str(e)}")

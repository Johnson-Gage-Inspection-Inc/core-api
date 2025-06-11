# routes/pyro_assets.py
from flask.views import MethodView
from flask_smorest import Blueprint
from qualer_sdk.api import AssetsApi

from utils.auth import require_auth
from utils.qualer_client import make_qualer_client
from utils.schemas import AssetToAssetSchema

blp = Blueprint("pyro-assets", __name__, url_prefix="/")


@blp.route("/pyro-assets")
class PyroAssets(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Pyro"])
    @blp.response(200, AssetToAssetSchema(many=True))
    def get(self):
        """
        Retrieve assets from the Pyro asset pool in Qualer.

        This endpoint fetches all assets belonging to the "Pyro" asset pool
        (ID: 620646) from the Qualer system. The assets returned include
        various details about each asset in the pool.

        **Returns**:
        - **list**: A list of asset objects from the Pyro asset pool containing:
          - asset_id: Unique identifier for the asset
          - asset_name: Name of the asset
          - asset_pool_id: ID of the asset pool (620646 for Pyro)
          - Additional asset attributes as defined by Qualer API

        **Raises**:
        - **401**: If authentication token is invalid or missing
        - **500**: If there's an error communicating with the Qualer API

        **Example**: GET /pyro-assets with Authorization: Bearer <token>

        **Response**: Array of asset objects from Pyro asset pool (ID: 620646)
        """
        client = make_qualer_client()
        assets_api = AssetsApi(client)
        return assets_api.get_asset_by_asset_pool(asset_pool_id=620646)

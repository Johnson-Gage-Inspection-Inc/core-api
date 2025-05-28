# routes/pyro_assets.py
from flask.views import MethodView
from flask_smorest import Blueprint
from qualer_sdk import AssetsApi
from schemas import AssetToAssetSchema
from utils.auth import require_auth
from utils.qualer_client import make_qualer_client


blp = Blueprint("pyro-assets", __name__, url_prefix="/")

@blp.route("/pyro-assets")
class PyroAssets(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}])
    @blp.response(200, AssetToAssetSchema(many=True))
    def get(self):
        client = make_qualer_client()
        assets_api = AssetsApi(client)
        return assets_api.get_asset_by_asset_pool(asset_pool_id=620646)
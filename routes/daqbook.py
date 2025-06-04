# routes/daqbook.py
from flask.views import MethodView
from flask_smorest import Blueprint

from utils.auth import require_auth
from utils.daqbook import refresh_daqbook_offsets

blp = Blueprint("daqbook", __name__, url_prefix="/refresh")


@blp.route("/daqbook-offsets")
class DaqbookRefresh(MethodView):
    @require_auth
    def post(self):
        """
        Refresh DAQbook offset data from SharePoint.

        Triggers the pipeline to download updated DAQbook files from SharePoint
        and update the database with the latest offset calibration data.
        """
        refresh_daqbook_offsets()
        return {"status": "success", "message": "DAQbook offsets refreshed"}

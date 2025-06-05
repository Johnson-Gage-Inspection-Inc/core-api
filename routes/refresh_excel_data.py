# routes/refresh_excel_data.py
"""
Route for unified refresh of Excel data from SharePoint.

This endpoint triggers a unified refresh of all Excel data categories:
1. WireSetCerts (Pyro/WireSetCerts.xlsx)
2. WireOffsets (wire certificate files in Pyro_Standards)
3. DaqbookOffsets (DAQbook files in Pyro_Standards)
"""

from flask.views import MethodView
from flask_smorest import Blueprint

from utils.auth import require_auth
from utils.unified_refresh import refresh_all_updated_categories

blp = Blueprint("refresh_excel_data", __name__, url_prefix="/refresh-excel-data")


@blp.route("/", methods=["POST"])
class ExcelRefresh(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["System"])
    def post(self):
        """
        Refresh all Excel data from SharePoint.

        This endpoint performs a unified refresh of multiple data categories:
        - WireSetCerts: The WireSetCerts.xlsx mapping file
        - WireOffsets: Wire certificate .xls files for wire lot calibration
        - DaqbookOffsets: DAQbook calibration files (J1_*, K5_*, etc.)

        Files are only processed if they've been modified in the past 24 hours.

        Returns:
            dict: A comprehensive report of the refresh operation, including:
                - Which categories were updated
                - Number of files processed
                - Success/error status for each category
                - A summary line for quick status reporting
        """
        try:
            return refresh_all_updated_categories()
        except Exception as e:
            # Return 500 error for unhandled exceptions
            from flask import jsonify

            return jsonify({"error": "Internal server error", "message": str(e)}), 500

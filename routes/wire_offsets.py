# routes/wire_offsets.py
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy import func

from db.models import WireOffset, WireSetCert
from utils.auth import require_auth
from utils.database import SessionLocal
from utils.schemas import WireOffsetSchema, WireSetCertSchema

blp = Blueprint("wire_offsets", __name__, url_prefix="/")


@blp.route("/wire-offsets/")
class WireOffsets(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Calibration"])
    @blp.response(200, WireOffsetSchema(many=True))
    def get(self):
        """
        Retrieve current wire offset calibration data.

        TODO: This should query the wire_offsets_current view (not yet created)
        to get the latest offset data for each wirelot/block combination.
        
        The view should handle the append-only nature of the table and return
        only the most recent entry for each wirelot/block pair.

        **Returns**:
        - **list**: A list of current offset objects containing:
          - wirelot: Wire lot identifier
          - block: Block type ("Top" or "Bottom")  
          - col1-col5: Latest offset reading values
          - created_at: Timestamp of the measurement

        **Raises**:
          - **401**: If authentication token is invalid or missing
          - **500**: If there's an error communicating with the database
        """
        db = None
        try:
            db = SessionLocal()
              # TODO: Replace this with a query to wire_offsets_current view
            # For now, get latest entry for each wirelot/block combination
            
            # Subquery to get latest timestamp for each wirelot/block
            latest_subq = (
                db.query(
                    WireOffset.wirelot,
                    WireOffset.block,
                    func.max(WireOffset.created_at).label('max_created_at')
                )
                .group_by(WireOffset.wirelot, WireOffset.block)
                .subquery()
            )
            
            # Join with main table to get full records
            offsets = (
                db.query(WireOffset)
                .join(
                    latest_subq,
                    (WireOffset.wirelot == latest_subq.c.wirelot) &
                    (WireOffset.block == latest_subq.c.block) &
                    (WireOffset.created_at == latest_subq.c.max_created_at)
                )
                .all()
            )

            # Convert to dict format
            result = []
            for offset in offsets:
                result.append(
                    {
                        "id": offset.id,
                        "wirelot": offset.wirelot,
                        "block": offset.block,
                        "col1": float(offset.col1) if offset.col1 is not None else None,
                        "col2": float(offset.col2) if offset.col2 is not None else None,
                        "col3": float(offset.col3) if offset.col3 is not None else None,
                        "col4": float(offset.col4) if offset.col4 is not None else None,
                        "col5": float(offset.col5) if offset.col5 is not None else None,
                        "created_at": offset.created_at.isoformat() if offset.created_at else None,
                    }
                )

            return result

        except Exception as e:
            # Log the error and return 500
            import logging

            logging.error(f"Database error in wire-offsets: {e}")
            from flask_smorest import abort

            abort(500, message="Internal server error")
        finally:
            if db:
                db.close()


@blp.route("/wire-offsets/<string:wirelot>")
class WireOffsetsByWirelot(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Calibration"])
    @blp.response(200, WireOffsetSchema(many=True))
    def get(self, wirelot):
        """
        Retrieve current wire offset data for a specific wire lot.

        TODO: This should also use the wire_offsets_current view.

        **Parameters**:
        - **wirelot**: Wire lot identifier to filter by

        **Returns**:
        - **list**: A list of current offset objects for the specified wire lot

        **Raises**:
          - **401**: If authentication token is invalid or missing
          - **500**: If there's an error communicating with the database
        """
        db = None
        try:
            db = SessionLocal()
              # TODO: Replace with view query
            # For now, get latest entry for each block of this wirelot
            
            latest_subq = (
                db.query(
                    WireOffset.block,
                    func.max(WireOffset.created_at).label('max_created_at')
                )
                .filter(WireOffset.wirelot == wirelot)
                .group_by(WireOffset.block)
                .subquery()
            )
            
            offsets = (
                db.query(WireOffset)
                .filter(WireOffset.wirelot == wirelot)
                .join(
                    latest_subq,
                    (WireOffset.block == latest_subq.c.block) &
                    (WireOffset.created_at == latest_subq.c.max_created_at)
                )
                .all()
            )

            # Convert to dict format
            result = []
            for offset in offsets:
                result.append(
                    {
                        "id": offset.id,
                        "wirelot": offset.wirelot,
                        "block": offset.block,
                        "col1": float(offset.col1) if offset.col1 is not None else None,
                        "col2": float(offset.col2) if offset.col2 is not None else None,
                        "col3": float(offset.col3) if offset.col3 is not None else None,
                        "col4": float(offset.col4) if offset.col4 is not None else None,
                        "col5": float(offset.col5) if offset.col5 is not None else None,
                        "created_at": offset.created_at.isoformat() if offset.created_at else None,
                    }
                )

            return result

        except Exception as e:
            # Log the error and return 500
            import logging

            logging.error(f"Database error in wire-offsets/{wirelot}: {e}")
            from flask_smorest import abort

            abort(500, message="Internal server error")
        finally:
            if db:
                db.close()


@blp.route("/wire-set-certs/")
class WireSetCerts(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Calibration"])
    @blp.response(200, WireSetCertSchema(many=True))
    def get(self):
        """
        Retrieve wire set certificate mappings.

        TODO: Returns cached data from WireSetCerts.xlsx showing which
        serial numbers belong to which wire set groups.

        **Returns**:
        - **list**: A list of wire set certificate mappings

        **Raises**:
          - **401**: If authentication token is invalid or missing
          - **500**: If there's an error communicating with the database
        """
        db = None
        try:
            db = SessionLocal()
            certs = db.query(WireSetCert).all()

            # Convert to dict format
            result = []
            for cert in certs:
                result.append(
                    {
                        "id": cert.id,
                        "serial_number": cert.serial_number,
                        "wire_set_group": cert.wire_set_group,
                        "created_at": cert.created_at.isoformat() if cert.created_at else None,
                        "updated_at": cert.updated_at.isoformat() if cert.updated_at else None,
                    }
                )

            return result

        except Exception as e:
            # Log the error and return 500
            import logging

            logging.error(f"Database error in wire-set-certs: {e}")
            from flask_smorest import abort

            abort(500, message="Internal server error")
        finally:
            if db:
                db.close()


@blp.route("/wire-set-certs/refresh")
class WireSetCertsRefresh(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["System"])
    @blp.response(200)
    def post(self):
        """
        Refresh wire set certificate data from SharePoint.

        TODO: This endpoint should:
        1. Download the latest WireSetCerts.xlsx from SharePoint
        2. Parse the file to extract serial number -> wire set group mappings
        3. Update the wire_set_certs table with new/changed data
        4. Return a summary of the refresh operation

        **Returns**:
        - **dict**: Summary of refresh operation (records added/updated/errors)

        **Raises**:
          - **401**: If authentication token is invalid or missing
          - **500**: If there's an error during the refresh process
        """
        try:
            # TODO: Implement wire set cert refresh logic
            # from utils.wire_set_cert_refresher import refresh_wire_set_certs
            # result = refresh_wire_set_certs()
            
            # Placeholder response
            result = {
                "status": "success",
                "message": "Wire set certificate refresh not yet implemented",
                "records_processed": 0,
                "records_added": 0,
                "records_updated": 0,
                "errors": []
            }
            
            return result

        except Exception as e:
            # Log the error and return 500
            import logging

            logging.error(f"Error in wire-set-certs refresh: {e}")
            from flask_smorest import abort

            abort(500, message="Internal server error")

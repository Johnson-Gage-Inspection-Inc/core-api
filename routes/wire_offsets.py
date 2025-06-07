# routes/wire_offsets.py
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy import text
from werkzeug.exceptions import HTTPException

from db.models import WireSetCert
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

        Uses the wire_offsets_current view to get the latest correction factors
        for each wire lot and temperature combination.

        **Returns**:
        - **list**: A list of current offset objects containing:
          - traceability_no: Wire lot identifier (e.g., "072513A")
          - nominal_temp: Temperature in Celsius
          - correction_factor: Wire correction factor
          - created_at: Timestamp of the measurement
          - updated_by: User who last updated the source file

        **Raises**:
          - **401**: If authentication token is invalid or missing
          - **500**: If there's an error communicating with the database
        """
        db = None
        try:
            db = SessionLocal()
            # Query the wire_offsets_current view for most recent entries
            result = db.execute(
                text(
                    """
                SELECT id, traceability_no, nominal_temp, correction_factor,
                       created_at, updated_at, updated_by
                FROM wire_offsets_current
                ORDER BY traceability_no, nominal_temp
            """
                )
            ).fetchall()

            # Convert to dict format
            offsets = []
            for row in result:
                offsets.append(
                    {
                        "id": row.id,
                        "traceability_no": row.traceability_no,
                        "nominal_temp": float(row.nominal_temp),
                        "correction_factor": float(row.correction_factor),
                        "created_at": (
                            row.created_at.isoformat() if row.created_at else None
                        ),
                        "updated_at": (
                            row.updated_at.isoformat() if row.updated_at else None
                        ),
                        "updated_by": row.updated_by,
                    }
                )

            return offsets

        except Exception as e:
            # Log the error and return 500
            import logging

            logging.error(f"Database error in wire-offsets: {e}")
            from flask_smorest import abort

            abort(500, message="Internal server error")
        finally:
            if db:
                db.close()


@blp.route("/wire-offsets/<string:traceability_no>")
class WireOffsetsByTraceabilityNo(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Calibration"])
    @blp.response(200, WireOffsetSchema(many=True))
    def get(self, traceability_no):
        """
        Retrieve current wire offset data for a specific wire lot.

        Uses the wire_offsets_current view filtered by traceability number.

        **Parameters**:
        - **traceability_no**: Wire lot identifier to filter by (e.g., "072513A")

        **Returns**:
        - **list**: A list of current offset objects for the specified wire lot

        **Raises**:
          - **401**: If authentication token is invalid or missing
          - **404**: If no wire lot found with that traceability number
          - **500**: If there's an error communicating with the database
        """

        db = None
        try:
            db = SessionLocal()

            # Query the wire_offsets_current view for specific traceability number
            result = db.execute(
                text(
                    """
                SELECT id, traceability_no, nominal_temp, correction_factor,
                       created_at, updated_at, updated_by
                FROM wire_offsets_current
                WHERE traceability_no = :traceability_no
                ORDER BY nominal_temp
            """
                ),
                {"traceability_no": traceability_no},
            ).fetchall()

            if not result:
                abort(
                    404,
                    message=f"No wire offsets found for traceability number: {traceability_no}",
                )

            # Convert to dict format
            offsets = []
            for row in result:
                offsets.append(
                    {
                        "id": row.id,
                        "traceability_no": row.traceability_no,
                        "nominal_temp": float(row.nominal_temp),
                        "correction_factor": float(row.correction_factor),
                        "created_at": (
                            row.created_at.isoformat() if row.created_at else None
                        ),
                        "updated_at": (
                            row.updated_at.isoformat() if row.updated_at else None
                        ),
                        "updated_by": row.updated_by,
                    }
                )

            return offsets

        except Exception as e:
            # Check if this is an abort exception (werkzeug HTTPException)

            if isinstance(e, HTTPException):
                raise

            # Log the error and return 500 for actual database errors
            import logging

            logging.error(f"Database error in wire-offsets/{traceability_no}: {e}")
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
            certs = db.query(
                WireSetCert
            ).all()  # Return the SQLAlchemy objects directly - Marshmallow will handle serialization
            return certs

        except Exception as e:
            # Log the error and return 500
            import logging

            logging.error(f"Database error in wire-set-certs: {e}")
            from flask_smorest import abort

            abort(500, message="Internal server error")
        finally:
            if db:
                db.close()


@blp.route("/wire-set-certs/<string:serial_number>")
class WireSetCertBySerial(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Calibration"])
    @blp.response(200, WireSetCertSchema)
    def get(self, serial_number):
        """
        Retrieve wire set certification data for a specific serial number.

        **Parameters**:
        - **serial_number**: Wire serial number to look up (e.g., "J201")

        **Returns**:
        - **object**: Wire set cert object with all certification details

        **Raises**:
          - **401**: If authentication token is invalid or missing
          - **404**: If no wire found with that serial number
          - **500**: If there's an error communicating with the database
        """
        db = None
        try:
            db = SessionLocal()
            cert = (
                db.query(WireSetCert)
                .filter(WireSetCert.serial_number == serial_number)
                .first()
            )

            if not cert:
                from flask_smorest import abort

                abort(
                    404,
                    message=f"No wire set cert found for serial number: {serial_number}",
                )

            # Return the SQLAlchemy object directly - Marshmallow will handle serialization
            return cert

        except Exception as e:
            # Log the error and return 500
            import logging

            logging.error(f"Database error in wire-set-certs/{serial_number}: {e}")
            from flask_smorest import abort

            abort(500, message="Internal server error")
        finally:
            if db:
                db.close()

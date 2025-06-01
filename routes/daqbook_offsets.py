# routes/daqbook_offsets.py
from flask.views import MethodView
from flask_smorest import Blueprint

from db.models import DaqbookOffset
from utils.auth import require_auth
from utils.database import SessionLocal
from utils.schemas import DaqbookOffsetSchema

blp = Blueprint("daqbook_offsets", __name__, url_prefix="/")


@blp.route("/daqbook-offsets/")
class DaqbookOffsets(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Calibration"])
    @blp.response(200, DaqbookOffsetSchema(many=True))
    def get(self):
        """
        Retrieve all daqbook offset calibration data.

        This endpoint fetches all offset data from all daqbooks. The data includes
        temperature points, measurement points, and offset readings that can be
        used for calibration calculations.

        **Returns**:
        - **list**: A list of offset objects containing:
          - tn: Test number/daqbook identifier
          - temp: Temperature point in degrees
          - point: Measurement point number (1-40)
          - reading: Offset reading value (delta between raw value and expected)

        **Raises**:
          - **401**: If authentication token is invalid or missing
          - **500**: If there's an error communicating with the database

        **Example**: GET /daqbook-offsets/ with Authorization: Bearer <token>        **Response**:        **Response**:
          - Array of offset objects with tn, temp, point, and reading values
        """
        db = None
        try:
            db = SessionLocal()
            offsets = db.query(DaqbookOffset).all()

            # Convert to dict format
            result = []
            for offset in offsets:
                result.append(
                    {
                        "tn": offset.tn,
                        "temp": float(offset.temp),
                        "point": offset.point,
                        "reading": float(offset.reading),
                    }
                )

            return result

        except Exception as e:
            # Log the error and return 500
            import logging

            logging.error(f"Database error in daqbook-offsets: {e}")
            from flask_smorest import abort

            abort(500, message="Internal server error")
        finally:
            if db:
                db.close()


@blp.route("/daqbook-offsets/<string:tn>")
class DaqbookOffsetsByTN(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Calibration"])
    @blp.response(200, DaqbookOffsetSchema(many=True))
    def get(self, tn):
        """
        Retrieve daqbook offset data for a specific test number.

        **Parameters**:
        - **tn**: Test number/daqbook identifier to filter by

        **Returns**:
        - **list**: A list of offset objects for the specified test number

        **Raises**:
          - **401**: If authentication token is invalid or missing
          - **500**: If there's an error communicating with the database        **Example**: GET /daqbook-offsets/J10325 with Authorization: Bearer <token>
        """
        db = None
        try:
            db = SessionLocal()
            offsets = db.query(DaqbookOffset).filter(DaqbookOffset.tn == tn).all()

            # Convert to dict format
            result = []
            for offset in offsets:
                result.append(
                    {
                        "tn": offset.tn,
                        "temp": float(offset.temp),
                        "point": offset.point,
                        "reading": float(offset.reading),
                    }
                )

            return result

        except Exception as e:
            # Log the error and return 500
            import logging

            logging.error(f"Database error in daqbook-offsets/{tn}: {e}")
            from flask_smorest import abort

            abort(500, message="Internal server error")
        finally:
            if db:
                db.close()

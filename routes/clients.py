# routes/clients.py
from typing import Any, List

import attr
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from qualer_sdk.api.clients.get_all_get_2 import sync as get_clients
from qualer_sdk.models import QualerApiModelsClientsToClientCompanyResponseModel

from utils.auth import require_auth
from utils.qualer_client import make_qualer_client

blp = Blueprint("clients", __name__, url_prefix="/")


@blp.route("/clients")
class Clients(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Qualer"])
    @blp.response(200)
    def get(self) -> List[dict[str, Any]]:
        """
        Retrieve all client companies from Qualer.

        This endpoint fetches all client companies from the Qualer system.
        The response includes company details such as ID, name, and other
        relevant information.

        **Returns**:
        - **list**: A list of client company objects containing:
          - company_id: Unique identifier for the client company
          - company_name: Name of the client company
          - account_number_text: Account number as text
          - Additional company attributes as defined by Qualer API

        **Raises**:
        - **401**: If authentication token is invalid or missing
        - **500**: If there's an error communicating with the Qualer API

        **Example**: GET /clients with Authorization: Bearer <token>

        **Response**: Array of client company objects with comprehensive company information
        """
        try:
            client = make_qualer_client()
            clients: List[QualerApiModelsClientsToClientCompanyResponseModel] = (
                get_clients(client=client)
            ) or []

            # Convert attrs models to dictionaries using attr.asdict()
            result = []
            for client_obj in clients:
                client_dict = attr.asdict(client_obj)
                # Filter out any Unset values that attrs might include
                filtered_dict = {
                    k: v
                    for k, v in client_dict.items()
                    if not (hasattr(v, "__class__") and "Unset" in str(type(v)))
                }
                result.append(filtered_dict)

            return result
        except Exception as e:
            abort(500, message=f"Error fetching clients: {str(e)}")

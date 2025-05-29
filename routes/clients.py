# routes/clients.py
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from qualer_sdk import ClientsApi
from utils.schemas import ClientCompanyResponseSchema
from utils.auth import require_auth
from utils.qualer_client import make_qualer_client


blp = Blueprint("clients", __name__, url_prefix="/")

@blp.route("/clients")
class Clients(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Qualer"])
    @blp.response(200, ClientCompanyResponseSchema(many=True))
    def get(self):
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
            api = ClientsApi(client)
            return api.get_all()
        except Exception as e:
            abort(500, message=f"Error fetching clients: {str(e)}")
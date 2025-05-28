# routes/employees.py
from flask.views import MethodView
from flask_smorest import Blueprint
from qualer_sdk import EmployeesApi
from qualer_sdk.models import QualerApiModelsClientsToEmployeeResponseModel
from schemas import EmployeesModel
from utils.auth import require_auth
from utils.qualer_client import make_qualer_client

blp = Blueprint("employees", __name__, url_prefix="/")

@blp.route("/employees")
class Employees(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}])
    @blp.response(200, EmployeesModel(many=True))
    def get(self):
        """
        Retrieve all active employees from Qualer.
        
        This endpoint fetches all employees from the Qualer system and filters out
        any employees that are marked as deleted. The response includes employee
        details such as ID, name, and other relevant information.
        
        **Returns**:
        - **list**: A list of employee objects containing:
          - employee_id: Unique identifier for the employee
          - name: Employee's full name  
          - is_deleted: Boolean indicating if employee is active
          - Additional employee attributes as defined by Qualer API
        
        **Raises**:
        - **401**: If authentication token is invalid or missing
        - **500**: If there's an error communicating with the Qualer API
        
        **Example**: GET /employees with Authorization: Bearer <token>
        
        **Response**: Array of employee objects with employee_id, name, is_deleted fields
        """
        client = make_qualer_client()

        employees_api = EmployeesApi(client)
        employees = employees_api.get_employees()
        assert isinstance(employees, list), "Expected a list of employees"
        Employee = QualerApiModelsClientsToEmployeeResponseModel
        assert all(isinstance(e, Employee) for e in employees)
        return [e for e in employees if not e.is_deleted]

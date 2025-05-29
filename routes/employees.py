# routes/employees.py
from flask.views import MethodView
from flask_smorest import Blueprint
from qualer_sdk import EmployeesApi
from qualer_sdk.models import QualerApiModelsClientsToEmployeeResponseModel
from schemas import EmployeeResponseSchema
from utils.auth import require_auth
from utils.qualer_client import make_qualer_client

blp = Blueprint("employees", __name__, url_prefix="/")

@blp.route("/employees")
class Employees(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}])
    @blp.response(200, EmployeeResponseSchema(many=True))
    def get(self):
        """
        Retrieve all active employees from Qualer.
        
        This endpoint fetches all employees from the Qualer system and filters out
        any employees that are marked as deleted. The response includes employee
        details such as ID, name, and other relevant information.

        **Returns**:
        - **list**: A list of employee objects containing:
          - employee_id: Unique identifier for the employee
          - name: Employee's full name (first_name + last_name)
          - first_name: Employee's first name
          - last_name: Employee's last name
          - company_id: Company identifier
          - login_email: Employee's login email
          - departments: List of department objects with id, name, and position
          - subscription_email: Email for subscriptions
          - subscription_phone: Phone for subscriptions
          - office_phone: Office phone number
          - is_locked: Boolean indicating if account is locked
          - image_url: URL to employee's image
          - alias: Employee's alias
          - title: Employee's job title
          - is_deleted: Boolean indicating if employee is deleted (always false in results)
          - last_seen_date_utc: Last seen date in ISO format
          - culture_name: Culture name
          - culture_ui_name: UI culture name
        
        **Raises**:
          - **401**: If authentication token is invalid or missing
          - **500**: If there's an error communicating with the Qualer API        **Example**: GET /employees with Authorization: Bearer <token>

        **Response**:
          - Array of employee objects with comprehensive employee information including id, name, contact details, and department assignments
        """        
        client = make_qualer_client()

        employees_api = EmployeesApi(client)
        employees = employees_api.get_employees()
        assert isinstance(employees, list), "Expected a list of employees"
        Employee = QualerApiModelsClientsToEmployeeResponseModel
        assert all(isinstance(e, Employee) for e in employees)
        
        # Return active employees (raw SDK objects)
        return [e for e in employees if not e.is_deleted]

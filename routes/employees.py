# routes/employees.py
import attr
from flask.views import MethodView
from flask_smorest import Blueprint
from qualer_sdk.api.employees.get_employees_get_2 import sync as get_employees
from qualer_sdk.models import QualerApiModelsClientsToEmployeeResponseModel

from utils.auth import require_auth
from utils.qualer_client import make_qualer_client

blp = Blueprint("employees", __name__, url_prefix="/")


@blp.route("/employees")
class Employees(MethodView):
    @require_auth
    @blp.doc(security=[{"BearerAuth": []}], tags=["Qualer"])
    @blp.response(200)
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
          - **500**: If there's an error communicating with the Qualer API
          **Example**: GET /employees with Authorization: Bearer <token>
          **Response**:
          - Array of employee objects with comprehensive employee information including id, name, contact details, and department assignments
        """
        client = make_qualer_client()
        employees = get_employees(client=client)
        assert isinstance(employees, list), "Expected a list of employees"
        Employee = QualerApiModelsClientsToEmployeeResponseModel
        assert all(isinstance(e, Employee) for e in employees)

        # Filter active employees and convert to dictionaries
        active_employees = [e for e in employees if not e.is_deleted]

        result = []
        for employee in active_employees:
            employee_dict = attr.asdict(employee)
            # Filter out any Unset values that attrs might include
            filtered_dict = {
                k: v
                for k, v in employee_dict.items()
                if not (hasattr(v, "__class__") and "Unset" in str(type(v)))
            }
            result.append(filtered_dict)

        return result

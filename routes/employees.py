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
        Get a list of all employees from Qualer who are not marked as deleted.
        """
        client = make_qualer_client()

        employees_api = EmployeesApi(client)
        employees = employees_api.get_employees()
        assert isinstance(employees, list), "Expected a list of employees"
        Employee = QualerApiModelsClientsToEmployeeResponseModel
        assert all(isinstance(e, Employee) for e in employees)
        return [e for e in employees if not e.is_deleted]

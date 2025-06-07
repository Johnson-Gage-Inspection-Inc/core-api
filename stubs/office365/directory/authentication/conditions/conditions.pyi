from _typeshed import Incomplete
from office365.directory.authentication.conditions.applications import AuthenticationConditionsApplications as AuthenticationConditionsApplications
from office365.runtime.client_value import ClientValue as ClientValue

class AuthenticationConditions(ClientValue):
    applications: Incomplete
    def __init__(self, applications=...) -> None: ...

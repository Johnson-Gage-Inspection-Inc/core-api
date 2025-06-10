from _typeshed import Incomplete
from office365.directory.applications.roles.role import AppRole as AppRole
from office365.runtime.client_value_collection import (
    ClientValueCollection as ClientValueCollection,
)

class AppRoleCollection(ClientValueCollection[AppRole]):
    def __init__(self, initial_values: Incomplete | None = None) -> None: ...
    def __getitem__(self, key: str) -> AppRole: ...
    def get_by_value(self, value: str) -> AppRole: ...

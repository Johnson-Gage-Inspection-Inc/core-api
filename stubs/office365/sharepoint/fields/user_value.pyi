from office365.sharepoint.fields.lookup_value import (
    FieldLookupValue as FieldLookupValue,
)
from office365.sharepoint.principal.users.user import User as User

class FieldUserValue(FieldLookupValue):
    def __init__(self, user_id) -> None: ...
    @staticmethod
    def from_user(user: User) -> FieldUserValue: ...

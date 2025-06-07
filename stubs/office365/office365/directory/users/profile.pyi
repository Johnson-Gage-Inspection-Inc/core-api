from _typeshed import Incomplete
from office365.directory.users.password_profile import (
    PasswordProfile as PasswordProfile,
)
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class UserProfile(ClientValue):
    userPrincipalName: Incomplete
    passwordProfile: Incomplete
    mailNickname: Incomplete
    displayName: Incomplete
    accountEnabled: Incomplete
    givenName: Incomplete
    companyName: Incomplete
    businessPhones: Incomplete
    officeLocation: Incomplete
    city: Incomplete
    country: Incomplete
    def __init__(
        self,
        principal_name,
        password,
        display_name: Incomplete | None = None,
        given_name: Incomplete | None = None,
        company_name: Incomplete | None = None,
        business_phones: Incomplete | None = None,
        office_location: Incomplete | None = None,
        city: Incomplete | None = None,
        country: Incomplete | None = None,
        account_enabled: bool = False,
    ) -> None: ...

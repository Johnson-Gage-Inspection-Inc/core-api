from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class PasswordProfile(ClientValue):
    password: Incomplete
    forceChangePasswordNextSignIn: Incomplete
    forceChangePasswordNextSignInWithMfa: Incomplete
    def __init__(self, password: Incomplete | None = None, force_change_password_next_sign_in: Incomplete | None = None, force_change_password_next_sign_in_with_mfa: Incomplete | None = None) -> None: ...

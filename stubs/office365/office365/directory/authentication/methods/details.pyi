from office365.entity import Entity as Entity

class UserRegistrationDetails(Entity):
    @property
    def is_admin(self) -> bool | None: ...
    @property
    def is_mfa_registered(self) -> bool | None: ...
    @property
    def is_passwordless_capable(self) -> bool | None: ...
    @property
    def is_sspr_capable(self) -> bool | None: ...
    @property
    def is_sspr_enabled(self) -> bool | None: ...
    @property
    def user_display_name(self) -> str | None: ...
    @property
    def user_preferred_method_for_secondary_authentication(self) -> str | None: ...
    @property
    def user_principal_name(self) -> str | None: ...
    @property
    def user_type(self) -> str | None: ...

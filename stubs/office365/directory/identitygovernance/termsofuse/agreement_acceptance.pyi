from office365.entity import Entity as Entity

class AgreementAcceptance(Entity):
    @property
    def user_principal_name(self) -> str | None: ...

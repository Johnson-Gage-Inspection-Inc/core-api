from office365.runtime.client_value import ClientValue as ClientValue

class CAnonymousLinkUseLimit(ClientValue):
    @property
    def entity_type_name(self) -> str: ...

class CExternalSharingEnforcement(ClientValue):
    @property
    def entity_type_name(self) -> str: ...

from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ContextWebInformation(ClientValue):
    FormDigestValue: Incomplete
    FormDigestTimeoutSeconds: Incomplete
    LibraryVersion: Incomplete
    SiteFullUrl: Incomplete
    SupportedSchemaVersions: Incomplete
    WebFullUrl: Incomplete
    def __init__(self, form_digest_value: Incomplete | None = None, form_digest_timeout_secs: Incomplete | None = None) -> None: ...
    @property
    def is_valid(self): ...

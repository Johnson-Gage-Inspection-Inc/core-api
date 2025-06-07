from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class UploadSession(ClientValue):
    uploadUrl: Incomplete
    expirationDateTime: Incomplete
    nextExpectedRanges: Incomplete
    def __init__(self, upload_url: Incomplete | None = None, expiration_datetime: Incomplete | None = None, next_expected_ranges: Incomplete | None = None) -> None: ...

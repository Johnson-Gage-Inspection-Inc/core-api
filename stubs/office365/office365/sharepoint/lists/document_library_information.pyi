from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class DocumentLibraryInformation(ClientValue):
    Title: Incomplete
    AbsoluteUrl: Incomplete
    ServerRelativeUrl: Incomplete
    DriveId: Incomplete
    FromCrossFarm: Incomplete
    IsDefaultDocumentLibrary: Incomplete
    def __init__(
        self,
        title: Incomplete | None = None,
        absolute_url: Incomplete | None = None,
        server_relative_url: Incomplete | None = None,
        drive_id: Incomplete | None = None,
        from_cross_farm: Incomplete | None = None,
        is_default_document_library: Incomplete | None = None,
    ) -> None: ...

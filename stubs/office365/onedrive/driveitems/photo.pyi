from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class Photo(ClientValue):
    cameraMake: Incomplete
    cameraModel: Incomplete
    def __init__(self, camera_make: Incomplete | None = None, camera_model: Incomplete | None = None) -> None: ...

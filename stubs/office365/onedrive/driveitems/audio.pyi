from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class Audio(ClientValue):
    album: Incomplete
    albumArtist: Incomplete
    artist: Incomplete
    bitrate: Incomplete
    def __init__(self, album: Incomplete | None = None, album_artist: Incomplete | None = None, artist: Incomplete | None = None, bitrate: Incomplete | None = None) -> None: ...

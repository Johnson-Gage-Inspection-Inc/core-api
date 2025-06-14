from _typeshed import Incomplete

class TokenResponse:
    accessToken: Incomplete
    tokenType: Incomplete
    def __init__(
        self,
        access_token: Incomplete | None = None,
        token_type: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    @property
    def is_valid(self): ...
    @property
    def authorization_header(self): ...
    @staticmethod
    def from_json(value): ...

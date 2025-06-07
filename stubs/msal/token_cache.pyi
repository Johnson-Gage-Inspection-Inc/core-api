from .authority import canonicalize as canonicalize
from .oauth2cli.oauth2 import Client as Client
from .oauth2cli.oidc import (
    decode_id_token as decode_id_token,
    decode_part as decode_part,
)
from _typeshed import Incomplete
from collections.abc import Generator

logger: Incomplete

def is_subdict_of(small, big): ...

class TokenCache:
    class CredentialType:
        ACCESS_TOKEN: str
        REFRESH_TOKEN: str
        ACCOUNT: str
        ID_TOKEN: str
        APP_METADATA: str

    class AuthorityType:
        ADFS: str
        MSSTS: str

    key_makers: Incomplete
    def __init__(self) -> None: ...
    def search(
        self,
        credential_type,
        target: Incomplete | None = None,
        query: Incomplete | None = None,
        *,
        now: Incomplete | None = None,
    ) -> Generator[Incomplete]: ...
    def find(
        self,
        credential_type,
        target: Incomplete | None = None,
        query: Incomplete | None = None,
        *,
        now: Incomplete | None = None,
    ): ...
    def add(self, event, now: Incomplete | None = None): ...
    def modify(
        self, credential_type, old_entry, new_key_value_pairs: Incomplete | None = None
    ) -> None: ...
    def remove_rt(self, rt_item): ...
    def update_rt(self, rt_item, new_rt): ...
    def remove_at(self, at_item): ...
    def remove_idt(self, idt_item): ...
    def remove_account(self, account_item): ...

class SerializableTokenCache(TokenCache):
    has_state_changed: bool
    def add(self, event, **kwargs) -> None: ...
    def modify(
        self, credential_type, old_entry, new_key_value_pairs: Incomplete | None = None
    ) -> None: ...
    def deserialize(self, state: Optional[str]) -> None: ...
    def serialize(self) -> str: ...

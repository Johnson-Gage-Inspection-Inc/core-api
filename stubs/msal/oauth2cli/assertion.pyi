from _typeshed import Incomplete

logger: Incomplete

class AssertionCreator:
    def create_normal_assertion(
        self,
        audience,
        issuer,
        subject,
        expires_at: Incomplete | None = None,
        expires_in: int = 600,
        issued_at: Incomplete | None = None,
        assertion_id: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def create_regenerative_assertion(
        self,
        audience,
        issuer,
        subject: Incomplete | None = None,
        expires_in: int = 600,
        **kwargs,
    ): ...

class AutoRefresher:
    def __init__(self, factory, expires_in: int = 540) -> None: ...
    def __call__(self): ...

class JwtAssertionCreator(AssertionCreator):
    key: Incomplete
    algorithm: Incomplete
    headers: Incomplete
    def __init__(
        self,
        key,
        algorithm,
        sha1_thumbprint: Incomplete | None = None,
        headers: Incomplete | None = None,
        *,
        sha256_thumbprint: Incomplete | None = None,
    ) -> None: ...
    def create_normal_assertion(
        self,
        audience,
        issuer,
        subject: Incomplete | None = None,
        expires_at: Incomplete | None = None,
        expires_in: int = 600,
        issued_at: Incomplete | None = None,
        assertion_id: Incomplete | None = None,
        not_before: Incomplete | None = None,
        additional_claims: Incomplete | None = None,
        **kwargs,
    ): ...

Signer = AssertionCreator
JwtSigner = JwtAssertionCreator

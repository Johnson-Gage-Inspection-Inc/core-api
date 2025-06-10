from _typeshed import Incomplete

LOGGING_SECRET_LVL: int
LOGGING_SECRET_NAME: str

def ensure_debug_secrets() -> None: ...

class LoggerContext:
    @classmethod
    def logger(cls, method: Incomplete | None = None): ...

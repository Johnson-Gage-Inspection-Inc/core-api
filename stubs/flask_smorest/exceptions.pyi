import werkzeug.exceptions as wexc

class FlaskSmorestError(Exception): ...
class MissingAPIParameterError(FlaskSmorestError): ...

class NotModified(wexc.HTTPException, FlaskSmorestError):
    code: int
    description: str

class PreconditionRequired(wexc.PreconditionRequired, FlaskSmorestError):
    description: str

class PreconditionFailed(wexc.PreconditionFailed, FlaskSmorestError): ...
class CurrentApiNotAvailableError(FlaskSmorestError): ...

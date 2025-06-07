from .sku import SKU as SKU, __version__ as __version__
from _typeshed import Incomplete

logger: Incomplete
min_ver: Incomplete

class RedirectUriError(ValueError): ...
class TokenTypeError(ValueError): ...

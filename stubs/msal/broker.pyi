from _typeshed import Incomplete

from .sku import SKU as SKU
from .sku import __version__ as __version__

logger: Incomplete
min_ver: Incomplete

class RedirectUriError(ValueError): ...
class TokenTypeError(ValueError): ...

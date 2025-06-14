from .application import ClientApplication as ClientApplication
from .application import ConfidentialClientApplication as ConfidentialClientApplication
from .application import PublicClientApplication as PublicClientApplication
from .auth_scheme import PopAuthScheme as PopAuthScheme
from .managed_identity import (
    ArcPlatformNotSupportedError as ArcPlatformNotSupportedError,
)
from .managed_identity import ManagedIdentityClient as ManagedIdentityClient
from .managed_identity import ManagedIdentityError as ManagedIdentityError
from .managed_identity import (
    SystemAssignedManagedIdentity as SystemAssignedManagedIdentity,
)
from .managed_identity import UserAssignedManagedIdentity as UserAssignedManagedIdentity
from .oauth2cli.oauth2 import (
    BrowserInteractionTimeoutError as BrowserInteractionTimeoutError,
)
from .oauth2cli.oidc import IdTokenError as IdTokenError
from .oauth2cli.oidc import Prompt as Prompt
from .sku import __version__ as __version__
from .token_cache import SerializableTokenCache as SerializableTokenCache
from .token_cache import TokenCache as TokenCache

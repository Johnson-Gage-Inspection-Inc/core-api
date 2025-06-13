from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.post_asset_images_response_200 import (
    PostAssetImagesResponse200 as PostAssetImagesResponse200,
)
from ...types import Response as Response

def sync_detailed(
    id: int, *, client: AuthenticatedClient | Client
) -> Response[PostAssetImagesResponse200]: ...
def sync(
    id: int, *, client: AuthenticatedClient | Client
) -> PostAssetImagesResponse200 | None: ...
async def asyncio_detailed(
    id: int, *, client: AuthenticatedClient | Client
) -> Response[PostAssetImagesResponse200]: ...
async def asyncio(
    id: int, *, client: AuthenticatedClient | Client
) -> PostAssetImagesResponse200 | None: ...

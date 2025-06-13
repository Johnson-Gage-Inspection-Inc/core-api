from ... import errors as errors
from ...client import AuthenticatedClient as AuthenticatedClient
from ...client import Client as Client
from ...models.qualer_api_models_asset_reservation_from_upsert_asset_reservation_model import (
    QualerApiModelsAssetReservationFromUpsertAssetReservationModel as QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
)
from ...models.qualer_api_models_asset_reservation_to_upsert_asset_reservation_response import (
    QualerApiModelsAssetReservationToUpsertAssetReservationResponse as QualerApiModelsAssetReservationToUpsertAssetReservationResponse,
)
from ...types import Response as Response

def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
) -> Response[QualerApiModelsAssetReservationToUpsertAssetReservationResponse]: ...
def sync(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
) -> QualerApiModelsAssetReservationToUpsertAssetReservationResponse | None: ...
async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
) -> Response[QualerApiModelsAssetReservationToUpsertAssetReservationResponse]: ...
async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: QualerApiModelsAssetReservationFromUpsertAssetReservationModel,
) -> QualerApiModelsAssetReservationToUpsertAssetReservationResponse | None: ...

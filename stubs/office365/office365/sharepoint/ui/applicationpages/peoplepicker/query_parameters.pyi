from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.principal.source import PrincipalSource as PrincipalSource
from office365.sharepoint.principal.type import PrincipalType as PrincipalType

class ClientPeoplePickerQueryParameters(ClientValue):
    QueryString: Incomplete
    AllowEmailAddresses: Incomplete
    AllowMultipleEntities: Incomplete
    AllowOnlyEmailAddresses: Incomplete
    AllUrlZones: Incomplete
    EnabledClaimProviders: Incomplete
    ForceClaims: Incomplete
    MaximumEntitySuggestions: Incomplete
    PrincipalSource: Incomplete
    PrincipalType: Incomplete
    UrlZone: Incomplete
    UrlZoneSpecified: Incomplete
    SharePointGroupID: Incomplete
    def __init__(
        self,
        query_string,
        allow_emai_addresses: bool = True,
        allow_multiple_entities: bool = True,
        allow_only_email_addresses: bool = False,
        all_url_zones: bool = False,
        enabled_claim_providers: Incomplete | None = None,
        force_claims: bool = False,
        maximum_entity_suggestions: int = 1,
        principal_source=...,
        principal_type=...,
        url_zone: int = 0,
        url_zone_specified: bool = False,
        sharepoint_group_id: int = 0,
    ) -> None: ...
    @property
    def entity_type_name(self): ...

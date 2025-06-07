from _typeshed import Incomplete
from office365.directory.permissions.identity_set import IdentitySet as IdentitySet
from office365.runtime.client_value import ClientValue as ClientValue

class SharingInvitation(ClientValue):
    email: Incomplete
    invitedBy: Incomplete
    redeemedBy: Incomplete
    signInRequired: Incomplete
    def __init__(
        self,
        email: Incomplete | None = None,
        invited_by=...,
        redeemed_by: Incomplete | None = None,
        signin_required: Incomplete | None = None,
    ) -> None: ...

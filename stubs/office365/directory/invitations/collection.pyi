from _typeshed import Incomplete
from office365.directory.invitations.invitation import Invitation as Invitation
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.queries.create_entity import CreateEntityQuery as CreateEntityQuery

class InvitationCollection(EntityCollection[Invitation]):
    def __init__(self, context, resource_path: Incomplete | None = None) -> None: ...
    def create(self, invited_user_email_address, invite_redirect_url: Incomplete | None = None): ...

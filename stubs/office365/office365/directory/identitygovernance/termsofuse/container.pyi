from office365.directory.identitygovernance.termsofuse.agreement import (
    Agreement as Agreement,
)
from office365.directory.identitygovernance.termsofuse.agreement_acceptance import (
    AgreementAcceptance as AgreementAcceptance,
)
from office365.entity import Entity as Entity
from office365.entity_collection import EntityCollection as EntityCollection
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath

class TermsOfUseContainer(Entity):
    @property
    def agreements(self): ...
    @property
    def agreement_acceptances(self): ...

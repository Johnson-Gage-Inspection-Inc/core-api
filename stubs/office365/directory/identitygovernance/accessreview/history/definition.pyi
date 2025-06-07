from office365.directory.identitygovernance.accessreview.scope import AccessReviewScope as AccessReviewScope
from office365.entity import Entity as Entity
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class AccessReviewHistoryDefinition(Entity):
    @property
    def scopes(self): ...

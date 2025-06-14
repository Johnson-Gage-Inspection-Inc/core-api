from office365.sharepoint.activities.action_facet import ActionFacet as ActionFacet
from office365.sharepoint.activities.facets.activity_time import (
    ActivityTimeFacet as ActivityTimeFacet,
)
from office365.sharepoint.activities.facets.coalesced import (
    CoalescedFacet as CoalescedFacet,
)
from office365.sharepoint.activities.facets.in_doc import InDocFacet as InDocFacet
from office365.sharepoint.activities.facets.resource import (
    ResourceFacet as ResourceFacet,
)
from office365.sharepoint.entity import Entity as Entity
from office365.sharepoint.sharing.principal import Principal as Principal

class SPActivityEntity(Entity):
    @property
    def action(self): ...
    @property
    def actor(self): ...
    @property
    def is_coalesced(self): ...
    @property
    def doc_details(self): ...
    @property
    def resource(self): ...
    @property
    def times(self): ...
    @property
    def property_ref_name(self): ...
    @property
    def entity_type_name(self): ...
    def set_property(self, name, value, persist_changes: bool = True): ...

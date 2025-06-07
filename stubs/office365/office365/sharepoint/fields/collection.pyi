from _typeshed import Incomplete
from office365.runtime.paths.service_operation import (
    ServiceOperationPath as ServiceOperationPath,
)
from office365.runtime.queries.create_entity import (
    CreateEntityQuery as CreateEntityQuery,
)
from office365.runtime.queries.service_operation import (
    ServiceOperationQuery as ServiceOperationQuery,
)
from office365.sharepoint.entity_collection import EntityCollection as EntityCollection
from office365.sharepoint.fields.calculated import FieldCalculated as FieldCalculated
from office365.sharepoint.fields.creation_information import (
    FieldCreationInformation as FieldCreationInformation,
)
from office365.sharepoint.fields.date_time import FieldDateTime as FieldDateTime
from office365.sharepoint.fields.field import Field as Field
from office365.sharepoint.fields.geolocation import FieldGeolocation as FieldGeolocation
from office365.sharepoint.fields.number import FieldNumber as FieldNumber
from office365.sharepoint.fields.text import FieldText as FieldText
from office365.sharepoint.fields.type import FieldType as FieldType
from office365.sharepoint.fields.url import FieldUrl as FieldUrl
from office365.sharepoint.fields.user import FieldUser as FieldUser
from office365.sharepoint.fields.xmlSchemaFieldCreationInformation import (
    XmlSchemaFieldCreationInformation as XmlSchemaFieldCreationInformation,
)
from office365.sharepoint.lists.list import List as List
from office365.sharepoint.taxonomy.field import TaxonomyField as TaxonomyField
from office365.sharepoint.taxonomy.sets.set import TermSet as TermSet
from office365.sharepoint.taxonomy.stores.store import TermStore as TermStore
from office365.sharepoint.webs.web import Web as Web

class FieldCollection(EntityCollection[Field]):
    def __init__(
        self,
        context,
        resource_path: Incomplete | None = None,
        parent: Incomplete | None = None,
    ) -> None: ...
    def add_calculated(self, title, formula, description: Incomplete | None = None): ...
    def add_datetime(
        self, title: str, description: str | None = None
    ) -> FieldDateTime: ...
    def add_geolocation_field(
        self, title: str, description: str | None = None
    ) -> FieldGeolocation: ...
    def add_number(self, title: str, description: str | None = None) -> FieldNumber: ...
    def add_url_field(self, title: str, description: str | None = None) -> FieldUrl: ...
    def add_lookup_field(
        self, title, lookup_list, lookup_field_name, allow_multiple_values: bool = False
    ): ...
    def add_choice_field(self, title, values, multiple_values: bool = False): ...
    def add_user_field(self, title: str) -> FieldUser: ...
    def add_text_field(self, title: str) -> FieldText: ...
    def add_dependent_lookup_field(
        self, display_name, primary_lookup_field_id, show_field
    ): ...
    def add(self, field_create_information): ...
    def add_field(self, parameters, return_type: Incomplete | None = None): ...
    def create_taxonomy_field(
        self, name, term_set, allow_multiple_values: bool = False
    ): ...
    def create_field_as_xml(
        self, schema_xml, return_type: Incomplete | None = None
    ): ...
    def get_by_id(self, _id): ...
    def get_by_internal_name_or_title(self, value): ...
    def get_by_title(self, title): ...
    @property
    def parent(self) -> Web | List: ...

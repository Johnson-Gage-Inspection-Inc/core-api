from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class ListCreationInformation(ClientValue):
    Title: Incomplete
    Description: Incomplete
    BaseTemplate: Incomplete
    AllowContentTypes: Incomplete
    CustomSchemaXml: Incomplete
    DataSourceProperties: Incomplete
    DocumentTemplateType: Incomplete
    QuickLaunchOption: Incomplete
    TemplateFeatureId: Incomplete
    TemplateType: Incomplete
    def __init__(self, title: Incomplete | None = None, description: Incomplete | None = None, base_template: Incomplete | None = None, allow_content_types: bool = False, custom_schema_xml: Incomplete | None = None, document_template_type: Incomplete | None = None, quick_launch_option: Incomplete | None = None, template_feature_id: Incomplete | None = None, template_type: Incomplete | None = None) -> None: ...
    @property
    def entity_type_name(self): ...

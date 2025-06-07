from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class RenderListDataOptions:
    None_: int
    ContextInfo: int
    ListData: int
    ListSchema: int
    MenuView: int

class RenderListDataParameters(ClientValue):
    AddAllFields: Incomplete
    AddAllViewFields: Incomplete
    AddRegionalSettings: Incomplete
    AddRequiredFields: Incomplete
    AllowMultipleValueFilterForTaxonomyFields: Incomplete
    AudienceTarget: Incomplete
    DatesInUtc: Incomplete
    ExpandGroups: Incomplete
    ExpandUserField: Incomplete
    FilterOutChannelFoldersInDefaultDocLib: Incomplete
    RenderOptions: Incomplete
    RequireFolderColoringFields: Incomplete
    ShowStubFile: Incomplete
    ViewXml: Incomplete
    def __init__(
        self,
        add_all_fields: Incomplete | None = None,
        add_all_view_fields: Incomplete | None = None,
        add_regional_settings: Incomplete | None = None,
        add_required_fields: Incomplete | None = None,
        allow_multiple_value_filter_for_taxonomy_fields: Incomplete | None = None,
        audience_target: Incomplete | None = None,
        dates_in_utc: Incomplete | None = None,
        expand_groups: Incomplete | None = None,
        expand_user_field: Incomplete | None = None,
        filter_out_channel_folders_in_default_doc_lib: Incomplete | None = None,
        render_options: Incomplete | None = None,
        require_folder_coloring_fields: Incomplete | None = None,
        show_stub_file: Incomplete | None = None,
        view_xml: Incomplete | None = None,
    ) -> None: ...
    @property
    def entity_type_name(self): ...

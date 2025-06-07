from office365.runtime.client_object import ClientObject as ClientObject
from office365.sharepoint.ui.applicationpages.peoplepicker.entity_information_request import PickerEntityInformationRequest as PickerEntityInformationRequest

class PickerEntityInformation(ClientObject):
    @property
    def total_member_count(self) -> int | None: ...
    @property
    def entity(self): ...
    @property
    def entity_type_name(self): ...

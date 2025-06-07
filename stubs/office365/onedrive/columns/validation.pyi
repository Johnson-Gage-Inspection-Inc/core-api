from _typeshed import Incomplete
from office365.onedrive.columns.display_name_localization import DisplayNameLocalization as DisplayNameLocalization
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection

class ColumnValidation(ClientValue):
    formula: Incomplete
    descriptions: Incomplete
    defaultLanguage: Incomplete
    def __init__(self, formula: Incomplete | None = None, descriptions: Incomplete | None = None, default_language: Incomplete | None = None) -> None: ...

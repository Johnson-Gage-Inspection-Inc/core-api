from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.types.collections import StringCollection as StringCollection

class ChoiceColumn(ClientValue):
    allowTextEntry: Incomplete
    choices: Incomplete
    displayAs: Incomplete
    def __init__(self, allow_text_entry: bool = True, choices: Incomplete | None = None, display_as: Incomplete | None = None) -> None: ...

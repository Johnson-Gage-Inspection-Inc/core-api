from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue

class SubwebQuery(ClientValue):
    WebTemplateFilter: Incomplete
    ConfigurationFilter: Incomplete
    def __init__(self, configuration_filter: int = -1, web_template_filter: int = -1) -> None: ...

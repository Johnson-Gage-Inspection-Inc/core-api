from office365.communications.result_info import ResultInfo as ResultInfo
from office365.entity import Entity as Entity

class CommsOperation(Entity):
    @property
    def client_context(self): ...
    @property
    def result_info(self): ...

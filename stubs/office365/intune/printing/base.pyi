from office365.entity import Entity as Entity
from office365.intune.printing.capabilities import PrinterCapabilities as PrinterCapabilities

class PrinterBase(Entity):
    @property
    def capabilities(self): ...

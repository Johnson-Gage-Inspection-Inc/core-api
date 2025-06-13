from enum import Enum

class QualerApiModelsServiceOrdersToProviderServiceOrderResponseModelTimeframe(
    str, Enum
):
    ASSOONASPOSSIBLE = "AsSoonAsPossible"
    BEFOREDATE = "BeforeDate"
    ONDATETIME = "OnDateTime"
    URGENT = "Urgent"
    WITHINRANGE = "WithinRange"

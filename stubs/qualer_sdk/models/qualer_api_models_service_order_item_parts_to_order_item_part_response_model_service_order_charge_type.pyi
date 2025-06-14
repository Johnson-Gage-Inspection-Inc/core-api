from enum import Enum

class QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModelServiceOrderChargeType(
    str, Enum
):
    CHARGE = "Charge"
    LABOR = "Labor"
    PART = "Part"

from enum import Enum

class QualerApiModelsServiceOrdersFromOrderItemUpdateModelAsFoundResult(str, Enum):
    DONE = "Done"
    FAIL = "Fail"
    FAILAMBIGUOUS = "FailAmbiguous"
    FAILSIGNIFICANT = "FailSignificant"
    NOTAVAILABLE = "NotAvailable"
    PASS = "Pass"
    PASSADJUSTMENT = "PassAdjustment"
    PASSAMBIGUOUS = "PassAmbiguous"

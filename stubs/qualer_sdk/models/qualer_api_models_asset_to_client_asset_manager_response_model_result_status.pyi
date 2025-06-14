from enum import Enum

class QualerApiModelsAssetToClientAssetManagerResponseModelResultStatus(str, Enum):
    DONE = "Done"
    FAIL = "Fail"
    FAILAMBIGUOUS = "FailAmbiguous"
    FAILSIGNIFICANT = "FailSignificant"
    MISSED = "Missed"
    NOTAVAILABLE = "NotAvailable"
    PASS = "Pass"
    PASSADJUSTMENT = "PassAdjustment"
    PASSAMBIGUOUS = "PassAmbiguous"
    PENDING = "Pending"

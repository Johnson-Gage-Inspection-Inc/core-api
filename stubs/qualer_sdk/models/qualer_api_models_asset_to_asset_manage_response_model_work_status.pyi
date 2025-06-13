from enum import Enum

class QualerApiModelsAssetToAssetManageResponseModelWorkStatus(str, Enum):
    CLOSED = "Closed"
    COMPLETED = "Completed"
    DELAYED = "Delayed"
    INPROGRESS = "InProgress"
    LOCKED = "Locked"
    NEW = "New"
    PENDING = "Pending"
    WAIT = "Wait"
    WITHDRAWN = "Withdrawn"

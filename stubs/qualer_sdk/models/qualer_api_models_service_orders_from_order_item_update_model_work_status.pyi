from enum import Enum

class QualerApiModelsServiceOrdersFromOrderItemUpdateModelWorkStatus(str, Enum):
    CLOSED = "Closed"
    COMPLETED = "Completed"
    DELAYED = "Delayed"
    INPROGRESS = "InProgress"
    LOCKED = "Locked"
    NEW = "New"
    PENDING = "Pending"
    WAIT = "Wait"
    WITHDRAWN = "Withdrawn"

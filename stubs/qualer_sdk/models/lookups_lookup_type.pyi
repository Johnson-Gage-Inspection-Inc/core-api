from enum import Enum

class LookupsLookupType(str, Enum):
    ASSETCLASS = "AssetClass"
    ASSETCONDITION = "AssetCondition"
    ASSETCRITICALITY = "AssetCriticality"
    CANCELORDERREASONS = "CancelOrderReasons"
    CLIENTCATEGORY = "ClientCategory"
    CLIENTINVOICING = "ClientInvoicing"
    CLIENTSTANDING = "ClientStanding"
    INVENTORYCATEGORY = "InventoryCategory"
    INVENTORYUNIT = "InventoryUnit"
    ORDERDELAYEDSTATUS = "OrderDelayedStatus"
    ORDERITEMCLOSEDWORKSTATUS = "OrderItemClosedWorkStatus"
    ORDERITEMCOMPLETEDWORKSTATUS = "OrderItemCompletedWorkStatus"
    ORDERITEMDELAYWORKSTATUS = "OrderItemDelayWorkStatus"
    ORDERITEMINPROGRESSWORKSTATUS = "OrderItemInProgressWorkStatus"
    ORDERITEMLOCKEDWORKSTATUS = "OrderItemLockedWorkStatus"
    ORDERITEMWITHDRAWNWORKSTATUS = "OrderItemWithdrawnWorkStatus"

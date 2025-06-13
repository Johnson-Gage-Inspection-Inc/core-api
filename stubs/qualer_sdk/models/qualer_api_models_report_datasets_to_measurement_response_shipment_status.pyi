from enum import Enum

class QualerApiModelsReportDatasetsToMeasurementResponseShipmentStatus(str, Enum):
    DELIVERED = "Delivered"
    NOTSHIPPED = "NotShipped"
    ONSITE = "OnSite"
    PARTIALSHIPMENT = "PartialShipment"
    SHIPPED = "Shipped"

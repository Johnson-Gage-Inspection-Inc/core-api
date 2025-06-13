from enum import Enum

class QualerApiModelsReportDatasetsToMeasurementResponseToleranceType(str, Enum):
    FUNCTION = "Function"
    OFFSET = "Offset"
    PERCENTAGE = "Percentage"
    PERCENTAGEPLUS = "PercentagePlus"
    PPM = "Ppm"
    PPMPLUS = "PpmPlus"
    RANGE = "Range"

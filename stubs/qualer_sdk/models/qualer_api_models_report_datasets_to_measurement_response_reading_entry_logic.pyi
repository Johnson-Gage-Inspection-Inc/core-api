from enum import Enum

class QualerApiModelsReportDatasetsToMeasurementResponseReadingEntryLogic(str, Enum):
    DOUBLESUBSTITUTION = "DoubleSubstitution"
    MEASUREDVALUECONVERSION = "MeasuredValueConversion"
    MEASUREDVALUECONVERSIONDISPLAY = "MeasuredValueConversionDisplay"
    SINGLEVALUE = "SingleValue"
    TWOVALUES = "TwoValues"
    TWOVALUESANDRESULT = "TwoValuesAndResult"

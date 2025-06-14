from enum import Enum

class QualerApiModelsAssetToAssetServiceForecastModelOnWeekDays(str, Enum):
    EVERYDAY = "EveryDay"
    FRIDAY = "Friday"
    MONDAY = "Monday"
    NONE = "None"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    THURSDAY = "Thursday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    WEEKENDDAYS = "WeekendDays"
    WORKDAYS = "WorkDays"

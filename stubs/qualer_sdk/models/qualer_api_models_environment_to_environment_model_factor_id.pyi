from enum import Enum

class QualerApiModelsEnvironmentToEnvironmentModelFactorId(str, Enum):
    AIRBUOYANCY = "AirBuoyancy"
    AIRHUMIDITY = "AirHumidity"
    ALTITUDE = "Altitude"
    AMBIENTTEMPERATURE = "AmbientTemperature"
    BAROMETRICPRESSURE = "BarometricPressure"
    EVAPORATIONRATE = "EvaporationRate"
    LIGHTINTENSITY = "LightIntensity"
    NOISELEVEL = "NoiseLevel"
    PHLEVEL = "PhLevel"
    SOLARRADIATION = "SolarRadiation"
    WATERCONDUCTIVITY = "WaterConductivity"
    WATERTEMPERATURE = "WaterTemperature"
    WINDSPEED = "WindSpeed"
    ZFACTOR = "ZFactor"

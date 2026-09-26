"""
Нужно создать своё исключение:
class InvalidTelemetryError(Exception):    pass

А затем функцию:
def validate_humidity(humidity):    ...

Правила:
0 <= humidity <= 100 → вернуть humidity

humidity < 0
или
humidity > 100
→ raise InvalidTelemetryError("Humidity out of range")

Примеры:
validate_humidity(60)
# 60
validate_humidity(0)
# 0
validate_humidity(100)
# 100
validate_humidity(150)
# InvalidTelemetryError: Humidity out of range
"""
class InvalidTelemetryError(Exception):
    pass

def validate_humidity(humidity):
    if humidity < 0 or humidity > 100:
        raise InvalidTelemetryError("Humidity out of range")
    return humidity
print(validate_humidity(60))
print(validate_humidity(0))
print(validate_humidity(100))
print(validate_humidity(150))
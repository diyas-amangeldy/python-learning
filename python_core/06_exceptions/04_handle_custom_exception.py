class InvalidTelemetryError(Exception):
    pass


def validate_humidity(humidity):
    if humidity < 0 or humidity > 100:
        raise InvalidTelemetryError("Humidity out of range")

    return humidity

def process_humidity(humidity):
    try:
        return validate_humidity(humidity)
    except InvalidTelemetryError:
        return None

print(process_humidity(60))
print(process_humidity(100))
print(process_humidity(-100))

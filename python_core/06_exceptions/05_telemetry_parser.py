"""
контракт:
parse_telemetry({
    "temperature": "25",
    "humidity": "60"
})
# {"temperature": 25, "humidity": 60}
"""

class InvalidTelemetryError(Exception):
    pass


def parse_telemetry(data):

    try:
        temp=int(data["temperature"])
        humid=int(data["humidity"])
        container= {
            "temperature": temp,
            "humidity": humid
        }
        if temp < -50 or temp > 100 or humid < 0 or humid > 100:
            raise InvalidTelemetryError("Telemetry out of range")
        return container
    except ValueError:
        raise InvalidTelemetryError("Invalid telemetry value")
    except KeyError:
        raise InvalidTelemetryError("Missing telemetry field")



test1=parse_telemetry({
    "temperature": "25"
})
print(test1)
"""record = {
    "device_id": 10,
    "temperature": 25,
    "humidity": 60
}

Напиши функцию:

def transform_telemetry(record):
    ...

Она должна вернуть новый dict, где будут все исходные поля плюс:

"status"

Правила:

temperature > 30  → "hot"
temperature < 10  → "cold"
иначе             → "normal"

исходный record должен остаться тем же."""

record = {
    "device_id": 10,
    "temperature": 25,
    "humidity": 60
}

def transform_telemetry(record):
    transformed_record = {
    "device_id": record["device_id"],
    "temperature": record["temperature"],
    "humidity": record["humidity"]
    }
    if record["temperature"] > 30:
        transformed_record["status"] = "hot"
    elif record["temperature"] < 10:
        transformed_record["status"] = "cold"
    else:
        transformed_record["status"] = "normal"
    return transformed_record
print(transform_telemetry(record))
print(record)

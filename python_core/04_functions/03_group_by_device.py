"""records = [
    {"device_id": 1, "temperature": 20},
    {"device_id": 2, "temperature": 25},
    {"device_id": 1, "temperature": 22},
    {"device_id": 3, "temperature": 18},
    {"device_id": 2, "temperature": 27},
]

Напиши функцию:

def group_by_device(records):
    ...

Она должна вернуть:

{
    1: [
        {"device_id": 1, "temperature": 20},
        {"device_id": 1, "temperature": 22},
    ],
    2: [
        {"device_id": 2, "temperature": 25},
        {"device_id": 2, "temperature": 27},
    ],
    3: [
        {"device_id": 3, "temperature": 18},
    ],
}
"""

records = [
    {"device_id": 1, "temperature": 20},
    {"device_id": 2, "temperature": 25},
    {"device_id": 1, "temperature": 22},
    {"device_id": 3, "temperature": 18},
    {"device_id": 2, "temperature": 27},
]

def group_by_device(records):
    groups = {}
    for record in records:
        if record["device_id"] not in groups:
            groups[record["device_id"]]=[]
            groups[record["device_id"]].append(record)
    return groups
print(group_by_device(records))
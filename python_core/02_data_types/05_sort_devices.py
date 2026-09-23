devices = [
    {"name": "Sensor B", "priority": 1},
    {"name": "Sensor C", "priority": 2},
    {"name": "Sensor A", "priority": 1},
    {"name": "Sensor D", "priority": 2},
]
"""Нужно отсортировать:
сначала по priority от меньшего к большему;
если priority одинаковый — по name.
"""
print(sorted(devices, key=lambda device: (device["priority"], device["name"])))

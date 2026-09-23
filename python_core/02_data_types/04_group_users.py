users = [
    {"name": "Anna", "city": "Almaty"},
    {"name": "Bob", "city": "Astana"},
    {"name": "Diyas", "city": "Almaty"},
    {"name": "Kate", "city": "Astana"},
    {"name": "Alex", "city": "Shymkent"},
]
"""
Нужно получить:
{
    "Almaty": ["Anna", "Diyas"],
    "Astana": ["Bob", "Kate"],
    "Shymkent": ["Alex"]
}
"""
citizens = {}
for user in users:
    if user["city"] in citizens:
        citizens[user["city"]].append(user["name"])
    else:
        citizens[user["city"]] = []
        citizens[user["city"]].append(user["name"])
print(citizens)

"""
citizens = {}

for user in users:
    city = user["city"]
    name = user["name"]

    if city not in citizens:
        citizens[city] = []

    citizens[city].append(name)

print(citizens)
"""

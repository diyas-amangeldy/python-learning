"""
record = {
    "temperature": 25,
    "humidity": 60
}

Напиши функцию, которая принимает record и возвращает:

True

если одновременно:

temperature от -50 до 100 включительно
humidity от 0 до 100 включительно

иначе:

False"""

test1 = {
    "temperature": 25,
    "humidity": 60
}
"""
def validate(record):
    if  record["temperature"] >= -50 and record["temperature"] <= 100 and record["humidity"] >=0 and record["humidity"]<=100:
        return True
    else:
        return False
print(validate(test1))
"""
def validate(record):
    return (
        -50 <= record["temperature"] <= 100
        and 0 <= record["humidity"] <= 100
    )
print(validate(test1))
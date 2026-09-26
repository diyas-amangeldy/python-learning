"""
Задача: функция принимает уже готовое число temperature.
Если оно находится в диапазоне от -50 до 100 включительно, вернуть его.
Если температура вне диапазона — самостоятельно выбросить:
ValueError("Temperature out of range")
Примеры поведения:
validate_temperature(25)
# 25
validate_temperature(-50)
# -50
validate_temperature(100)
# 100
validate_temperature(150)
#
ValueError: Temperature out of range
"""

def validate_temperature(temperature):
    if temperature < -50 or temperature > 100:
        raise ValueError("Temperature out of range")
    return temperature

print(validate_temperature(25))
print(validate_temperature(50))
print(validate_temperature(100))
print(validate_temperature(150))
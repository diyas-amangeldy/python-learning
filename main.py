"""Напиши функцию:

def calculate_stats(numbers):
    ...

Условия:

без sum();
без min();
без max();
можно использовать len();
вернуть dict с ключами:
"sum"
"count"
"average"
"min"
"max"

Пока не обрабатывай пустой список. Это позже свяжем с exceptions.

Пример:

calculate_stats([10, 20, 30])

должно вернуть:

{
    "sum": 60,
    "count": 3,
    "average": 20,
    "min": 10,
    "max": 30
}"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def calculate_stats(numbers):
    total = 0
    count = 0
    max_num = numbers[0]
    min_num = numbers[0]
    for number in numbers:
        total += number
        count += 1
        if number > max_num:
            max_num = number
        if number < min_num:
            min_num = number
    average = total / count
    result = {"sum": total,
              "count": count,
              "average": average,
              "max": max_num,
              "min": min_num}
    return result
print(calculate_stats(numbers))
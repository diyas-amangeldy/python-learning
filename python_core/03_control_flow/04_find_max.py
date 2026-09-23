"""04_find_max.py

Есть:

numbers = [12, 5, 38, 7, 21, 44, 3]

Найди максимальное число без max() и без сортировки."""
numbers = [12, 5, 38, 7, 21, 44, 3]
max_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
print(max_num)
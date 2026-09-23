"""
Для чисел от 1 до 30:

если число делится на 3 — вывести Fizz;
если делится на 5 — вывести Buzz;
если делится одновременно на 3 и 5 — вывести FizzBuzz;
иначе вывести само число."""

for i in range (1,31):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz", i)
    elif i % 3 == 0:
        print("Fizz", i)
    elif i % 5 == 0:
        print("Buzz", i)
    else:
        print(i)

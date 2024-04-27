"""
Задача 1. Разработайте функцию, которая принимает целое число в качестве аргумента и
возвращает строку, содержащую это число и слово "компьютер"
в нужном склонении по падежам в зависимости от числа.
Например, при вводе числа 25 функция должна возвращать "25 компьютеров", для числа 41 — "41 компьютер",
а для числа 1048 — "1048 компьютеров".
"""


def computer(number: int) -> str:
    if number % 10 == 1 and number % 100 != 11:
        return f"{number} компьютер"
    elif (
        number % 10 >= 2
        and number % 10 <= 4
        and (number % 100 < 10 or number % 100 >= 20)
    ):
        return f"{number} компьютера"
    else:
        return f"{number} компьютеров"


print(computer(1))
print(computer(25))
print(computer(34))
print(computer(41))
print(computer(1048))

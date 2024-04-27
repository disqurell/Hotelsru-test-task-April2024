"""
Задача 3. Написать функцию/метод, которая возвращает массив простых чисел в диапазоне
(2 числа - минимальное и максимальное) заданных чисел.
Например, на вход переданы 2 числа: от 11 до 20
(диапазон считается включая граничные значения).
На выходе программа должна выдать [11, 13, 17, 19]
"""

from math import sqrt


def simple(n, m):
    result = []
    for i in range(n, m + 1):
        if i > 1:
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                result.append(i)
    return result


print(simple(11, 20))

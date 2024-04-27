"""
Задача 4. Написать метод, который в консоль выводит таблицу умножения.
На вход метод получает число, до которого выводит таблицу умножения.
В консоли должна появиться таблица. Например, если на вход пришло число 5, то получим:
   1   2   3   4   5
1  1   2   3   4   5
2  2   4   6   8   10
3  3   6   9   12  15
4  4   8   12  16  20
5  5   10  15  20  25
"""


def multiply_table(n: int):
    numbers = [i for i in range(1, n + 1)]
    result = [[" ", *numbers]]

    for number in numbers:
        row = [number * i for i in numbers]
        row.insert(0, number)
        result.append(row)

    return result


number = 5

result = multiply_table(number)
s = [[str(e) for e in row] for row in result]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = "\t".join("{{:{}}}".format(x) for x in lens)
table = [fmt.format(*row) for row in s]

print("\n".join(table))

"""
Output (for number = 5):

        1       2       3       4       5
1       1       2       3       4       5
2       2       4       6       8       10
3       3       6       9       12      15
4       4       8       12      16      20
5       5       10      15      20      25
"""

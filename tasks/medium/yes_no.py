"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""
some_list = [1, 2, 3, 1, 5, 2, 1, 7]


def yes_or_no(some):
    met = set()
    for i in some:
        if i in met:
            print("Yes")
        else:
            print("No")
            met.add(i)


if __name__ == '__main__':
    yes_or_no(some_list)

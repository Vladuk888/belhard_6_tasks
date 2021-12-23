"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(number):
    if (number & (number - 1)) == 0 and number != 0:
        return True
        return check_number(number)
    else:
        return False

#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


def fact(n):
    result = 1

    for number in range(1, n + 1):
        result *= number
    return result




print(fact(5))

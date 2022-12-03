
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_max(numbers))


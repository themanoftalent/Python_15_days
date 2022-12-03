#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#  This is a simple python program to calculate the area and perimeter of a circle.

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


def main():
    radius = float(input('Enter the radius of the circle: '))
    circle = Circle(radius)
    print('Area of the circle is: ', circle.area())
    print('Perimeter of the circle is: ', circle.perimeter())


if __name__ == "__main__":
    main()

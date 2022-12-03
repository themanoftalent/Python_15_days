
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __str__(self):
        return f"({self.x},{self.y})"


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return self.p1.distance(self.p2)

    def __str__(self):
        return f"{self.p1} -> {self.p2}"


p1 = Point(1, 1)
p2 = Point(4, 5)
line = Line(p1, p2)
print(line)
print(line.length())

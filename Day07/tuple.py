#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

def tuples():
    tuple1 = (1, 2, 3, 4, 5, 6)
    print(tuple1)
    print(tuple1[0])
    print(tuple1[1:3])
    print(tuple1[2:])
    print(tuple1[:3])
    print(tuple1[-1])
    print(tuple1[-3:])
    print(tuple1[:-3])
    print(tuple1[::2])
    print(tuple1[::-1])
    print(tuple1[::-2])
    print(len(tuple1))
    print(max(tuple1))
    print(min(tuple1))
    print(sum(tuple1))
    print(tuple1.index(3))
    print(tuple1.count(3))

    tuple2 = (1, 2, 3, 4, 5, 6)
    print(tuple1 == tuple2)
    print(tuple1 is tuple2)

    tuple3 = tuple1
    print(tuple1 == tuple3)
    print(tuple1 is tuple3)


def main():
    tuples()


if __name__ == "__main__":
    main()

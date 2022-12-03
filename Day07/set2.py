
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


def main():
    set1 = set(range(1, 7))
    set2 = set(range(3, 9))
    print(set1)
    print(set2)
    print(set1 & set2)
    print(set1 | set2)
    print(set1 - set2)
    print(set1 ^ set2)
    print(set1 <= set2)
    print(set1 < set2)
    print(set1 >= set2)
    print(set1 > set2)

if __name__ == "__main__":
    main()


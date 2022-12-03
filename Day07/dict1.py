#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

def main():
    number = int(input("Enter the number of students: "))
    score = 0
    for i in range(number):
        score += int(input("Enter the score: "))
    print("Average score is: ", score / number)


if __name__ == "main":
    main()

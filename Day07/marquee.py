
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import os
import time


def main():
    str = 'Welcome to myy world!'  #  This is a string
    while True:
        os.system('cls')
        print(str)
        time.sleep(0.2)
        str = str[1:] + str[0]



if __name__ == '__main__':
    main()

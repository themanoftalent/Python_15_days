#!/bin/python3

import math
import os
import random
import re
import sys

num = int(input('Enter a number: '))

result = 0
maximum = 0

i = 0
while i < num:
    if num & (1 << i):
        result += 1
        if result > maximum:
            maximum = result
    else:
        result = 0
    i += 1

print(maximum)

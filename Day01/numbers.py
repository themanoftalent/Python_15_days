#  !/usr/bin/python
# author: Mehmet Akif CIFTCI
#

import math  # This will import math module

anumber = 5 # This is a number

print(anumber) # This will print the number
print() # This will print a new line
print(type(anumber)) # This will print the type of the variable

print(type(5.0)) # This will print the type of the variable

c = 5 + 3j # This is a complex number
print(c + 3) # This will print the sum of the complex number and the number

print((isinstance(c, complex))) # This will print True if the variable is a complex number

print('==========================')
print(int(2.3))
print(float(5))
print((complex('3+5j')))

print('=========================')
# now
# Number        System	      Prefix
# Binary	     '0b'    or    '0B'
# Octal	         '0o'    or    '0O'
# Hexadecimal	 '0x'    or    '0X'


print((0b1101011))

print((0xFB + 0b10))

print((0o15))

# ===============================

print('')
print("abs(-45) : ", abs(-45))
print("abs(100.12) : ", abs(100.12))
print("abs(119) : ", abs(119))
print('=========================')

print("math.ceil(-45.17) : ", math.ceil(-45.17))
print("math.ceil(100.12) : ", math.ceil(100.12))
print("math.ceil(100.72) : ", math.ceil(100.72))
print("math.ceil(119L) : ", math.ceil(119))
print("math.ceil(math.pi) : ", math.ceil(math.pi))

print('=========================')

num = int(input('Enter a number : '))
# To take input from the user
# num = int(input("Display multiplication table of? "))
# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)

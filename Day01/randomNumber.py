#  !/usr/bin/python
# author: Mehmet Akif CIFTCI
#

import random

print(random.randrange(1, 20)) # 1 ile 20 arasında rastgele sayı üretir
print('==============================')

x = ['a', 'b', 'c', 'd', 'e'] # this is a list
print(random.choice(x))

random.shuffle(x)
print(x)

print('==============================')
print(random.random())
print('==============================')
print(random.randint(1, 2000))
print('==============================')
print(random.randrange(100))

print('==============================')

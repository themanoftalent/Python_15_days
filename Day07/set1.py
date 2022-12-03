#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

thisisaset = {"apple", "banana", "cherry"}
for x in thisisaset:
    print(x)

print("banana" in thisisaset)

thisisaset.add("orange")
print(thisisaset)

thisisaset.update(["orange", "mango", "grapes"])
print(thisisaset)

print(len(thisisaset))

thisisaset.remove("banana")
print(thisisaset)

thisisaset.discard("banana")
print(thisisaset)

x = thisisaset.pop()
print(x)

thisisaset.clear()
print(thisisaset)

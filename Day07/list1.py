#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#


# List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apple', 'Orange', 'Grape', 'Peach']

# Use a constructor
numbers2 = list((1, 2, 3, 4, 5))

print(numbers, numbers2)

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mango')
print(fruits)

# Remove from list
fruits.remove('Grape')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberry')
print(fruits)

# Change value
fruits[0] = 'Blueberry'
print(fruits)

# Remove with pop
fruits.pop(2)
print(fruits)

# Reverse list
fruits.reverse()
print(fruits)

# Sort list
fruits.sort()
print(fruits)

# Reverse sort
fruits.sort(reverse=True)
print(fruits)

# List can be nested
numbers = [1, 2, 3, 4, 5]
fruits = ['Apple', 'Orange', 'Grape', 'Peach']
vegetables = ['Lettuce', 'Cucumber', 'Carrot']
dirty_dozen = [numbers, fruits, vegetables]
print(dirty_dozen)

# Get value
print(dirty_dozen[1][1])

# List can be defined with different data types
mixed = [1, 2, 3, 'Apple', 'Orange', True, False, [1, 2, 3]]
print(mixed)

# List can be defined with different data types
mixed = [1, 2, 3, 'Apple', 'Orange', True, False, [1, 2, 3]]
print(mixed)


# Author: Mehmet Akif CIFCI

# This is about linear search algorithm. It is a simple algorithm that searches for an element in a list by checking each element in the list sequentially until a match is found or the whole list has been searched.

def linear_search(list, item):
    list_length = len(list)
    for i in range(list_length):
        if list[i] == item:
            return i
    return 'Not found'


myItem = int(input("Enter the item: "))
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('The item is in the {0}'.format(linear_search(myList, myItem)))

linear_search(myList, myItem)

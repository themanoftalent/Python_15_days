# AUTHOR: MEHMET AKIF CIFCI
# Find the Missing Number

# We have a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

def getMissingNo(A):
    n = len(A)
    total = (n + 1) * (n + 2) / 2
    sum_of_A = sum(A)
    return total - sum_of_A

# Driver program to test above function
A = [1, 2, 4, 5, 6]
miss = getMissingNo(A)
print(miss)

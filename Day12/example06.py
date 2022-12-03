# Author: Mehmet AKif Cifci

# This is about Jump Search
import math


def Jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1


# Driver Code
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
x = int(input("Enter the number to search: "))
# Function Call
result = Jump_search(arr, x)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", str(result))

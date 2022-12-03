# Author : Mehmet Akif Cifci

# linear search time complexity: O(n)
import time


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


times = []
for i in range(1000):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    start = time.time()
    linear_search(arr, 15)
    end = time.time()
    times.append(end - start)
print(sum(times) / len(times))  # Best case time complexity: O(1)  # Average case time complexity: O(n)  # Worst case time complexity: O(n)



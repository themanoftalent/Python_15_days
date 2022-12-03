# Author: Mehmet Akif Cifci

# Selection Sort simple example
def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

# Driver Code
arr = [64, 25, 12, 22, 11,1,6,3,7,12,67,9]
print(selectionSort(arr))

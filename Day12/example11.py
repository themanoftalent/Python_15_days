# Author: Mehmet Akif Cifci

# Bubble sort simple example

def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A) - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A



A = [5, 2, 4, 6, 1, 3, 9, 34, 1, 456, 23, 4, 8]
print(BubbleSort(A))

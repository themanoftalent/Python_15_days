# Author : Mehmet Akif Cifci
#Shell Sort

def shellSort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Driver Code
arr = [64, 25, 12, 22, 11,1,6,3,7,12,67,9]
print(shellSort(arr))

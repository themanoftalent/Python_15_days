# Author: Mehmet Akif Cifci

# Merge sort simple example
def merge_sort(items):
    """Merge sort"""
    if len(items) < 2:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)

def merge(left, right):
    """Merge"""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

if __name__ == '__main__':
    items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print(merge_sort(items))


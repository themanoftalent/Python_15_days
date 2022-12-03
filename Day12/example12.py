# Author: Mehmet Akif Cifci

# Insertion sort simple example

def insertion_sort(items):
    """Insertion sort"""
    for i in range(1, len(items)):
        j = i - 1
        key = items[i]
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key
    return items

if __name__ == '__main__':
    items = [35, 97, 12, 68, 55, 73, 81, 40]
    print(insertion_sort(items))


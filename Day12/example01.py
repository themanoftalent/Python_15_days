class searchMe:
    """ This is a docstring for searchMe class."""


def bin_search(items, elem):
    start = 0
    end = len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem < items[mid]:
            end = mid - 1
        elif elem > items[mid]:
            start = mid + 1
        else:
            return mid
    return -1


def seq_search(items: list, elem) -> int:
    """ English docstring for seq_search function. """
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


#
def seq_search(items, elem):
    """ This is a docstring for seq_search function."""
    for index, item in enumerate(items):
        if elem == item:
            return index
    return -1


search1 = searchMe()
print(search1.__doc__)
print(seq_search.__doc__)
print(bin_search.__doc__)
print(searchMe.__doc__)

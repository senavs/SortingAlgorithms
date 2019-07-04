from ..utils.functions import swap, partition

def selection(array, inplace=True):
    if not inplace:
        cp_array = array.copy()
        return selection(cp_array, inplace=True)

    for pivot in range(len(array)):
        for index in range(pivot, len(array)):
            if array[index] < array[pivot]:
                swap(array, pivot, index)
    return array

def bubble(array, inplace=True):
    if not inplace:
        cp_array = array.copy()
        return bubble(cp_array, inplace=True)

    if len(array) <= 1:
        return array
    for limit in range(len(array)):
        for index in range(1, len(array)-limit):
            if array[index] < array[index-1]:
                swap(array, index, index-1)
    return array

def insertion(array, inplace=True):
    if not inplace:
        cp_array = array.copy()
        return insertion(cp_array, inplace=True)

    if len(array) <= 1:
        return array
    for pivot in range(1, len(array)):
        for index in range(len(array[:pivot])-1, -1, -1):
            if array[pivot] < array[index]:
                swap(array, pivot, index)
                pivot = index
            else:
                break
    return array

def quicksort(array, inplace=True):
        
    def sort(array, start, end):   
        if start < end:
            index = partition(array, start, end)
            sort(array, start, index - 1)
            sort(array, index + 1, end)
        return

    if not inplace:
        array = array.copy()

    sort(array, 0, len(array)-1)
    return array

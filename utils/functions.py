# Swap two elements in an array
def swap(array, pos1, pos2):
	tmp = array[pos1]
	array[pos1] = array[pos2]
	array[pos2] = tmp

# Partition function to return pivot_index to quicksort algorithm
def partition(array, start, end):
    pivot_index = start
    pivot_value = array[end]
    for i in range(start, end):
        if array[i] < pivot_value:
            swap(array, i, pivot_index)
            pivot_index += 1
    swap(array, pivot_index, end)
    return pivot_index

# Swap two elements in an array
def swap(array, pos1, pos2):
	tmp = array[pos1]
	array[pos1] = array[pos2]
	array[pos2] = tmp

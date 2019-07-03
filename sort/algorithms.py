from ..utils.functions import swap

def selection(array, inplace=False):
	if not inplace:
		cp_array = array.copy()
		return selection(cp_array, inplace=True)

	for pivot in range(len(array)):
		for index in range(pivot, len(array)):
			if array[index] < array[pivot]:
				swap(array, pivot, index)
	return array

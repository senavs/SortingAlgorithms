from ..utils.functions import swap

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

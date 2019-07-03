from ..utils.functions import swap

def selection(array):
	for pivot in range(len(array)):
		for index in range(pivot, len(array)):
			if array[index] < array[pivot]:
				swap(array, pivot, index)

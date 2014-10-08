def biggest_difference(arr):
	min = arr[0]
	max = arr[0]
	for element in arr:
		if min > element:
			min = element
		if max < element:
			max = element
		difference = - (max - min)
	return difference
print(biggest_difference([-10, -9, -1]))
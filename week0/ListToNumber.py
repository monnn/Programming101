def list_to_number(digits):
	number = ""
	for one_digit in digits:
		one_digit = str(one_digit)
		number += one_digit
	return number
print(list_to_number([1, 2, 3]))


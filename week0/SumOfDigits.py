def sum_of_digits(n):
	answer = 0
	str_n = str(n)
	for i in range(0, len(str_n)):
		digit = str_n[i]
		digit = int(digit)
		answer += digit
	return answer
print(sum_of_digits(67))
def is_increasing(seq):
	for i in range(1, len(seq)):
		if seq[i-1] < seq[i]:
			pass
		else:
			return False
	return True
print(is_increasing([1, 2, 3]))
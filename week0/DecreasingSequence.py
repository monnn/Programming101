def is_decreasing(seq):
    for i in range(1, len(seq)):
        if seq[i-1] > seq[i]:
            pass
        else:
            return False
    return True
print(is_decreasing([5, 4, 3, 2, 1]))

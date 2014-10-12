def nan_expand(n):
    if n == 0:
        return ""
    else:
        b = "NaN"
        a = n * "Not a "
        return a + b
print(nan_expand(3))

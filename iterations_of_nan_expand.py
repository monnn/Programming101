def iterations_of_nan_expand(n):
    answer = 0
    if n.count("Not a ") == 0:
        return False
    elif n == "":
        return answer
    else:
        counter = n.count("Not a ")
        if n.count("NaN") == 1:
            answer = counter
        return answer
print(iterations_of_nan_expand("Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN"))

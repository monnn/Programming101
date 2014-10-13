def zero_insert(n):
    n = str(n)
    result = ""
    for i in range(1, len(n)):
        first_digit = n[i-1]
        second_digit = n[i]
        if second_digit != n[len(n) - 1]:
            if first_digit == second_digit or (int(first_digit) + int(second_digit)) % 10 == 0:
                result += str(first_digit) + "0"
            else:
                result += str(first_digit)
        else:
            result += str(first_digit)
            result += str(second_digit)
    return result
print(zero_insert(116457))

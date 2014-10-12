def contains_digits(number, digits):
    lenth = len(digits)
    while number > 0:
        for one_digit in digits:
            single_digit = number % 10
            if one_digit == single_digit:
                lenth -= 1
                number = number // 10
            else:
                number = number // 10
    return lenth == 0
print(contains_digits(123878543, [1, 2, 3]))

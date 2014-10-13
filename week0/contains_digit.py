def contains_digit(number, digit):
    while number > 0:
        single_digit = number % 10
        if digit == single_digit:
            return True
        else:
            number = number // 10
    return False
print(contains_digit(123878543, 0))

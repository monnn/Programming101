def is_int_palindrome(n):
    number = n
    reversed_number = 0
    while n > 0:
        last_digit = n % 10
        reversed_number = reversed_number * 10 + last_digit
        n = n // 10
    if number == reversed_number:
        return True
    else:
        return False
print(is_int_palindrome(2442))

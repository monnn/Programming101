def prepare_meal(n):
    result = ""
    while n > 0:
        if n % 3 == 0 and n % 5 == 0:
            result += "spam and eggs "
            n /= 15
        if n % 3 == 0:
            result += "spam "
            n /= 3
        if n % 5 == 0:
            result += "eggs "
            n /= 5
    return result
print(prepare_meal(27))

def prime_number_of_divisors(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += 1
        else:
            return True
    for i in range(2, sum):
        if sum % i == 0:
            return False
        else:
            return True
print(prime_number_of_divisors(9))

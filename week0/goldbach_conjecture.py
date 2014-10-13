def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True

def goldbach(n):
    array = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if i + j == n and is_prime(i) is True and is_prime(j) is True:
                if i <= j:
                    array.append((i, j))
                else:
                    array.append((j, i))
    for m in range(0, len(array) - 1):
        for n in range(0, len(array) - 1):
            if array[m] == array[n]:
                array.remove(array[m])
    return array
print(goldbach(10))

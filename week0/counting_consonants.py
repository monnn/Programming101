def count_consonants(str):
    sum_of_consonants = 1
    consonants = "bcdfghjklmnpqrstvwxz"
    for i in range(0, len(str)):
        for j in range(0, len(consonants)):
            if str[i] == consonants[j]:
                sum_of_consonants += 1
    return sum_of_consonants
print(count_consonants("Python"))

def count_vowels(str):
    sum_of_vowels = 0
    vowels = "aieoyu"
    for i in range(0, len(str)):
        for j in range(0, len(vowels)):
            if str[i] == vowels[j]:
                sum_of_vowels += 1
    return sum_of_vowels
print(count_vowels("Python"))

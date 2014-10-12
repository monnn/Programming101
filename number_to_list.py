def number_to_list(n):
    array = []
    n = str(n)
    for i in range(0, len(n)):
        array.append(int(n[i]))
    return array
print(number_to_list(123023))

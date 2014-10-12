def is_number_balanced(n):
    n = str(n)
    first_sum = 0
    second_sum = 0
    middle = len(n) / 2
    for i in range(0, middle + 1):
        n = int(n)
        first_sum += n[i]
        print(first_sum)
    for i in range(middle, len(n) + 1):
        second_sum += n[i]
        print(second_sum)

def is_number_balanced(n):
    n = str(n)
    first_sum = 0
    second_sum = 0
    middle = len(n) // 2
    for i in range(0, middle):
        #n = int(n)
        first_sum += int(n[i])
    print(first_sum)
    if len(n) % 2 == 0:
        for j in range(middle, len(n)):
            second_sum += int(n[j])
        print(second_sum)
        if first_sum == second_sum:
            return True
        else:
            return False
    else:
        for j in range(middle + 1, len(n)):
            second_sum += int(n[j])
        print(second_sum)
        if first_sum == second_sum:
            return True
        else:
            return False
print(is_number_balanced(1238033))

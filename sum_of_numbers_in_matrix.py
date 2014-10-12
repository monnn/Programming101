def sum_matrix(m):
    sum_of_matrix = 0
    for i in m:
        sum_of_matrix += sum(i)
    return sum_of_matrix
print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def sum_in_each_row(matrix):
    sum_in_each_row = True
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if sum(matrix[i]) != sum(matrix[j]):
                sum_in_each_row = False
            else:
                pass
    return sum_in_each_row
print(sum_in_each_row([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))

def sum_in_each_column(matrix):
    sum_in_each_column = True
    sum_row = matrix[0, 0] + matrix[1, 0]
    for m in range(0, len(matrix)):
        for n in range(0, m):
            if sum_row != matrix[m, n]:
                sum_in_each_column = False
            else:
                pass
    return sum_in_each_column
print(sum_in_each_column([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))

#def magic_square(matrix):

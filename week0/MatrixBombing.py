def matrix_bombing_plan(m):
    for row in range(0, len(m)):
        for cell in range(0, len(str(m))):
            #print(m[row, cell])
            for cells in m:
                #if cells == cell[]

print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

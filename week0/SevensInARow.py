def sevens_in_a_row(arr, n):
    if arr[n-1] == 7:
        return True
    else:
        return False
print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))

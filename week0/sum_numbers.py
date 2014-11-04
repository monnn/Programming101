def sum_numbers(filename):
    sum = 0
    file = open(filename, "r")
    content = file.read()
    array = content.split(' ')
    '''a = array[0]
    a = a.replace('[', '')
    array[0] = a
    b = array[len(array) - 1]
    b = b.replace(']', '') 
    array[len(array) - 1] = b'''
    for i in range(0, len(array) - 1):
        array[i] = int(array[i])
    for j in range(0, len(array)):
        sum += int(array[j])
    return sum
    file.close()
print(sum_numbers("some.txt"))

def sum_numbers(filename):
    file = open(filename, "r")
    content = file.read()
    #content = int(content)
    array = content.split(', ')
    for i in range(0, len(array)):
        array[i] = int(array[i])
    for i in array:
        sum(i)
    print(sum(i))
    file.close()
print(sum_numbers("test.txt"))

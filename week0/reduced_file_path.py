def reduce_file_path(path):
    path = path.replace('/./', '/')
    path = path.replace('//', '/')
    reduced_path = path.split("/")
    if ".." in reduced_path:
        for i in range(1, len(reduced_path) - 1):
            if reduced_path[i] == "..":
                reduced_path.pop(i - 1)
                reduced_path.pop(i - 1)
    del reduced_path[-1]
    del reduced_path[0]
    reduced = ""
    for element in reduced_path:
        reduced += "/"
        reduced += element
    return reduced
print(reduce_file_path("/home//radorado/code/./hackbulgaria/week0/../"))

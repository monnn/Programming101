def reduce_file_path(path):
     path = path.replace('/./', '/')
     return path
print(reduce_file_path("/home//radorado/code/./hackbulgaria/week0/../"))
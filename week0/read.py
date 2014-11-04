filename = "file.txt"
file = open(filename, "r")
content = file.read()
print(content)
file.close()
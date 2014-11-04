filename = "file.txt"
file = open(filename, "w")
contents = ["Python is awesome", "You should check it out!"]
file.write("\n".join(contents))
file.close()
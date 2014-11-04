import sys


def main():
    for i in range (1, len(sys.argv)):
        filename = sys.argv[i]
        file = open(filename, "r")
        content = file.read()
        print(content)
        file_to_write = open("megatron.txt", "w")
        file_to_write.write("".join(content))
        print()
    file.close()

if __name__ == '__main__':
    main()
import sys


def main():
    for i in range (1, len(sys.argv)):
        filename = sys.argv[i]
        file = open(filename, "r")
        content = file.read()
        print(content)
        print()
    file.close()

if __name__ == '__main__':
    main()
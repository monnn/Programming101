import sys
import random


def main():
    filename = sys.argv[1]
    n = sys.argv[2]
    file = open(filename, "w")
    n = int(n)
    array = []
    for i in range(1, n):
        array.append(random.randint(1, n))
    array = str(array)
    file.write("".join(array))
    #print(array)
    file.close()

if __name__ == '__main__':
    main()
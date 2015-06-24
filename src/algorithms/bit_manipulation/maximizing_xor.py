import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def max_xor(L, R):
        maximum = 0

        for i in range(L, R + 1):
            for j in range(i, R + 1):
                value = i ^ j
                if maximum < value:
                    maximum = value

        return maximum


    def main():
        L = int(input())
        R = int(input())

        print(max_xor(L, R))


    if __name__ == "__main__":
        main()

'''


def max_xor(L, R):
    maximum = 0

    for i in range(L, R + 1):
        for j in range(i, R + 1):
            value = i ^ j
            if maximum < value:
                maximum = value

    return maximum


def main(argv):
    L, R = files.read_ints(argv[0])

    print(max_xor(L, R))


if __name__ == "__main__":
    main(sys.argv[1:])

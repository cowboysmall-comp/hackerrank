import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

import math


'''
    submitted code:

    def encrypt(text):
        L    = len(text)

        rows = math.floor(math.sqrt(L))
        cols = math.ceil(math.sqrt(L))

        if rows * cols < L:
            rows += 1

        A    = [['' for _ in range(rows)] for _ in range(cols)]

        idx  = 0
        for i in range(rows):
            for j in range(cols):
                if idx < L:
                    A[j][i] = text[idx]
                idx += 1

        return ' '.join(''.join(row) for row in A)


    def main():
        text = input().strip()

        print(encrypt(text))


    if __name__ == "__main__":
        main()

'''


def encrypt(text):
    L    = len(text)

    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))

    if rows * cols < L:
        rows += 1

    A    = [['' for _ in range(rows)] for _ in range(cols)]

    idx  = 0
    for i in range(rows):
        for j in range(cols):
            if idx < L:
                A[j][i] = text[idx]
            idx += 1

    return ' '.join(''.join(row) for row in A)


def main(argv):
    text = files.read_line(argv[0])

    print(encrypt(text))


if __name__ == "__main__":
    main(sys.argv[1:])

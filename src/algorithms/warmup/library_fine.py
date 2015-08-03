import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def library_fine(A, E):
        d = A[0] - E[0]
        m = A[1] - E[1]
        y = A[2] - E[2]


        if y > 0:
            return 10000

        if y == 0 and m > 0:
            return 500 * m

        if y == 0 and m == 0 and d > 0:
            return 15 * d

        return 0


    def main():
        A = [int(i) for i in input().split()]
        E = [int(i) for i in input().split()]

        print(library_fine(A, E))


    if __name__ == "__main__":
        main()

'''

def library_fine(A, E):
    d = A[0] - E[0]
    m = A[1] - E[1]
    y = A[2] - E[2]


    if y > 0:
        return 10000

    if y == 0 and m > 0:
        return 500 * m

    if y == 0 and m == 0 and d > 0:
        return 15 * d

    return 0


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    A     = lines[0]
    E     = lines[1]

    print(library_fine(A, E))


if __name__ == "__main__":
    main(sys.argv[1:])

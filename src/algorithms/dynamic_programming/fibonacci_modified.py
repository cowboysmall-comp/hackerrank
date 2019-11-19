import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def fibonacci_modified(A, B, N):
        F = [A, B]

        for i in range(2, N):
            F.append(F[-1] ** 2 + F[-2])

        return F[-1]


    def main():
        A, B, N = [int(i) for i in input().split()]

        print(fibonacci_modified(A, B, N))


    if __name__ == "__main__":
        main()

'''

def fibonacci_modified(A, B, N):
    F = [A, B]

    for i in range(2, N):
        F.append(F[-1] ** 2 + F[-2])

    return F[-1]


def main(argv):
    lines   = files.read_lines_of_ints(argv[0])
    A, B, N = lines[0]

    print(fibonacci_modified(A, B, N))


if __name__ == "__main__":
    main(sys.argv[1:])

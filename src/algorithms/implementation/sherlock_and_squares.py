import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files

import math


'''
    submitted code:

    def count_squares(A, B):
        A2 = math.sqrt(A)
        A3 = int(A2)
        return int(math.sqrt(B)) - A3 + (0 if (A2 - A3) > 0 else 1)


    def main():
        T = int(input())

        for i in range(T):
            A, B = [int(val) for val in input().split()]
            print(count_squares(A, B))


    if __name__ == "__main__":
        main()

'''

def count_squares(A, B):
    A2 = math.sqrt(A)
    A3 = int(A2)
    return int(math.sqrt(B)) - A3 + (0 if (A2 - A3) > 0 else 1)


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    for line in lines[1:]:
        print(count_squares(*line))


if __name__ == "__main__":
    main(sys.argv[1:])

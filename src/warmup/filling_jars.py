import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def filling_jars(operations, count):
        total = 0

        for operation in operations:
            total += (operation[1] - operation[0] + 1) * operation[2]

        return total // count


    def main():
        N, M  = [int(val) for val in input().split()]

        operations = []
        for i in range(M):
            operations.append([int(val) for val in input().split()])

        print(filling_jars(operations, N))


    if __name__ == "__main__":
        main()

'''


def filling_jars(operations, count):
    total = 0

    for operation in operations:
        total += (operation[1] - operation[0] + 1) * operation[2]

    return total // count


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, M  = lines[0]

    print(filling_jars(lines[1:], N))


if __name__ == "__main__":
    main(sys.argv[1:])

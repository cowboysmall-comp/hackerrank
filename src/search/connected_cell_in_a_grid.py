import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code:

    def max_region_size(A, m, n):
        maximum = 0

        def flood_fill(i, j):
            size = 0

            if A[i][j] == 1:
                A[i][j] = 'X'
                size   += 1

                for offset in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if 0 <= i + offset[0] <= m - 1 and 0 <= j + offset[1] <= n - 1:
                        size += flood_fill(i + offset[0], j + offset[1])

            return size

        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    maximum = max(flood_fill(i, j), maximum)

        return maximum


    def main():
        m = int(input())
        n = int(input())
        A = []
        for _ in range(m):
            A.append([int(i) for i in input().split()])

        print(max_region_size(A, m, n))


    if __name__ == "__main__":
        main()

'''


def max_region_size(A, m, n):
    maximum = 0

    def flood_fill(i, j):
        size = 0

        if A[i][j] == 1:
            A[i][j] = 'X'
            size   += 1

            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                if 0 <= i + offset[0] <= m - 1 and 0 <= j + offset[1] <= n - 1:
                    size += flood_fill(i + offset[0], j + offset[1])

        return size

    for i in range(m):
        for j in range(n):
            if A[i][j] == 1:
                maximum = max(flood_fill(i, j), maximum)

    return maximum


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    m     = lines[0][0]
    n     = lines[1][0]
    A     = lines[2:]

    print(max_region_size(A, m, n))


if __name__ == "__main__":
    main(sys.argv[1:])

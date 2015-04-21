import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code:

    def cavity_map(n, M):
        cmap = [[c for c in row] for row in M]

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if int(M[i][j]) > max([int(M[i - 1][j]), int(M[i + 1][j]), int(M[i][j - 1]), int(M[i][j + 1])]):
                    cmap[i][j] = 'X'

        return [''.join(row) for row in cmap]


    def main():
        n     = int(input())
        M     = [input() for _ in range(n)]

        print('\n'.join(cavity_map(n, M)))


    if __name__ == "__main__":
        main()

'''


def cavity_map(n, M):
    cmap = [[c for c in row] for row in M]

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if int(M[i][j]) > max([int(M[i - 1][j]), int(M[i + 1][j]), int(M[i][j - 1]), int(M[i][j + 1])]):
                cmap[i][j] = 'X'

    return [''.join(row) for row in cmap]


def main(argv):
    lines = files.read_lines(argv[0])
    n     = int(lines[0])
    M     = lines[1:]

    print('\n'.join(cavity_map(n, M)))


if __name__ == "__main__":
    main(sys.argv[1:])

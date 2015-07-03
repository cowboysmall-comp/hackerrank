import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def floyd(N, E):
        for n in range(1, N + 1):
            E[n][n] = 0

        for k in range(1, N + 1):
            for i in range(1, N + 1):
                if E[i][k] == 99999: continue
                for j in range(1, N + 1):
                    if E[i][j] > E[i][k] + E[k][j]:
                        E[i][j] = E[i][k] + E[k][j]


    def main():
        N, M = [int(i) for i in input().split()]

        E    = [[99999 for _ in range(N + 1)] for _ in range(N + 1)]

        for _ in range(M):
            x, y, r = [int(i) for i in input().split()]
            E[x][y] = r

        floyd(N, E)

        Q    = int(input())

        for _ in range(Q):
            a, b = [int(i) for i in input().split()]
            print(str(E[a][b]) if E[a][b] != 99999 else '-1')


    if __name__ == "__main__":
        main()

'''


def floyd(N, E):
    for n in range(1, N + 1):
        E[n][n] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            if E[i][k] == 99999: continue
            for j in range(1, N + 1):
                if E[i][j] > E[i][k] + E[k][j]:
                    E[i][j] = E[i][k] + E[k][j]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, M  = lines[0]

    E     = [[99999 for _ in range(N + 1)] for _ in range(N + 1)]

    for x, y, r in lines[1:M + 1]:
        E[x][y] = r

    floyd(N, E)

    Q     = lines[M + 1][0]

    for a, b in lines[M + 2:]:
        print(str(E[a][b]) if E[a][b] != 99999 else '-1')


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def count_decisions(N, M, F):
        start  = None
        finish = None

        for i in range(N):
            for j in range(M):
                if F[i][j] == 'M':
                    start  = (i, j)
                if F[i][j] == '*':
                    finish = (i, j)

        W = {start: 0}
        Q = [start]
        V = set()

        while Q and finish not in Q:
            p = Q.pop()
            V.add(p)

            R = []
            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                q = (p[0] + offset[0], p[1] + offset[1])
                if 0 <= q[0] <= N - 1 and 0 <= q[1] <= M - 1 and F[q[0]][q[1]] != 'X' and q not in V:
                    Q.append(q)
                    R.append(q)

            D = 1 if len(R) > 1 else 0
            for r in R:
                W[r] = W[p] + D

        return W[finish]


    def main():
        T = int(input())

        for _ in range(T):
            N, M = [int(i) for i in input().split()]
            F    = [[c for c in input()] for _ in range(N)]
            K    = int(input())
            print('Impressed' if count_decisions(N, M, F) == K else 'Oops!')


    if __name__ == "__main__":
        main()

'''


def count_decisions(N, M, F):
    start  = None
    finish = None

    for i in range(N):
        for j in range(M):
            if F[i][j] == 'M':
                start  = (i, j)
            if F[i][j] == '*':
                finish = (i, j)

    W = {start: 0}
    Q = [start]
    V = set()

    while Q and finish not in Q:
        p = Q.pop()
        V.add(p)

        R = []
        for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            q = (p[0] + offset[0], p[1] + offset[1])
            if 0 <= q[0] <= N - 1 and 0 <= q[1] <= M - 1 and F[q[0]][q[1]] != 'X' and q not in V:
                Q.append(q)
                R.append(q)

        D = 1 if len(R) > 1 else 0
        for r in R:
            W[r] = W[p] + D

    return W[finish]


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    count = 1
    for _ in range(T):
        N, M   = [int(i) for i in lines[count].split()]
        count += 1
        F      = lines[count:count + N]
        count += N
        K      = int(lines[count])
        count += 1
        print('Impressed' if count_decisions(N, M, F) == K else 'Oops!')


if __name__ == "__main__":
    main(sys.argv[1:])

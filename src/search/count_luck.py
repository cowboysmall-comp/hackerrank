import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from collections import deque


'''
    submitted code:

    def traverse_forest(N, M, F):
        V      = [[False for _ in range(M)] for _ in range(N)]
        B      = [[None for _ in range(M)] for _ in range(N)]

        start  = None
        finish = None


        for i in range(N):
            for j in range(M):
                if F[i][j] == 'M':
                    start  = (i, j)
                if F[i][j] == '*':
                    finish = (i, j)


        P      = [finish]
        Q      = deque([start])


        while Q and finish not in Q:
            p = Q.popleft()

            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                q = (p[0] + offset[0], p[1] + offset[1])
                if 0 <= q[0] <= N - 1 and 0 <= q[1] <= M - 1 and F[q[0]][q[1]] != 'X':
                    if not V[q[0]][q[1]]:
                        V[q[0]][q[1]] = True
                        B[q[0]][q[1]] = p
                        Q.append(q)



        while P[-1] != start:
            c = P[-1]
            P.append(B[c[0]][c[1]])



        P      = P[::-1]
        V      = [[False for _ in range(M)] for _ in range(N)]

        wand   = 0

        for p in P[:-1]:
            count         = 0
            V[p[0]][p[1]] = True

            for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                q = (p[0] + offset[0], p[1] + offset[1])
                if 0 <= q[0] <= N - 1 and 0 <= q[1] <= M - 1 and F[q[0]][q[1]] != 'X':
                    if not V[q[0]][q[1]]:
                        count += 1

            if count > 1:
                wand += 1


        return wand



    def main():
        T     = int(input())

        for _ in range(T):
            N, M = [int(i) for i in input().split()]
            F    = [[c for c in input()] for _ in range(N)]
            K    = int(input())
            print('Impressed' if traverse_forest(N, M, F) == K else 'Oops!')



    if __name__ == "__main__":
        main()

'''


def traverse_forest(N, M, F):
    V      = [[False for _ in range(M)] for _ in range(N)]
    B      = [[None for _ in range(M)] for _ in range(N)]

    start  = None
    finish = None


    for i in range(N):
        for j in range(M):
            if F[i][j] == 'M':
                start  = (i, j)
            if F[i][j] == '*':
                finish = (i, j)


    P      = [finish]
    Q      = deque([start])


    while Q and finish not in Q:
        p = Q.popleft()

        for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            q = (p[0] + offset[0], p[1] + offset[1])
            if 0 <= q[0] <= N - 1 and 0 <= q[1] <= M - 1 and F[q[0]][q[1]] != 'X':
                if not V[q[0]][q[1]]:
                    V[q[0]][q[1]] = True
                    B[q[0]][q[1]] = p
                    Q.append(q)


    while P[-1] != start:
        c = P[-1]
        P.append(B[c[0]][c[1]])


    P      = P[::-1]
    V      = [[False for _ in range(M)] for _ in range(N)]


    wand   = 0

    for p in P[:-1]:
        count         = 0
        V[p[0]][p[1]] = True

        for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            q = (p[0] + offset[0], p[1] + offset[1])
            if 0 <= q[0] <= N - 1 and 0 <= q[1] <= M - 1 and F[q[0]][q[1]] != 'X':
                if not V[q[0]][q[1]]:
                    count += 1

        if count > 1:
            wand += 1


    return wand



def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    count = 1
    for _ in range(T):
        N, M = [int(i) for i in lines[count].split()]
        count += 1
        F    = [[c for c in line] for line in lines[count:count + N]]
        count += N
        K    = int(lines[count])
        count += 1
        print('Impressed' if traverse_forest(N, M, F) == K else 'Oops!')



if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files

from collections import defaultdict, deque


'''
    submitted code:

    def breadth_first_search(G, P, S, T, N):
        V     = defaultdict(int)
        Q     = deque([S])

        V[S] += 1
        P[S]  = -1

        while Q:
            u = Q.popleft()
            for v in range(N):
                if V[v] == 0 and G[u][v] > 0:
                    Q.append(v)
                    P[v]  = u
                    V[v] += 1

        return V[T] == 1


    def floyd_fulkerson(G, S, T, N):
        P = [0 for _ in range(N)]
        M = 0

        while breadth_first_search(G, P, S, T, N):
            F = 999999

            v = T
            while v != S:
                u = P[v]
                F = min(F, G[u][v])
                v = P[v]

            v = T
            while v != S:
                u        = P[v]
                G[u][v] -= F
                G[v][u] += F
                v        = P[v]

            M += F

        return M


    def main():
        T = int(input())

        for _ in range(T):
            N, T, M = [int(i) for i in input().split()]

            E       = [[0 for _ in range((2 * N) + 2)] for _ in range((2 * N) + 2)]

            for _ in range(M):
                a, b = [int(i) for i in input().split()]
                E[(2 * a)][(2 * b) + 1] = 1
                E[(2 * b)][(2 * a) + 1] = 1

            for n in range(1, N + 1):
                E[0][(2 * n)]     = T
                E[(2 * n) + 1][1] = 1

            print(floyd_fulkerson(E, 0, 1, (2 * N) + 2))


    if __name__ == "__main__":
        main()

'''

def breadth_first_search(G, P, S, T, N):
    V     = defaultdict(int)
    Q     = deque([S])

    V[S] += 1
    P[S]  = -1

    while Q:
        u = Q.popleft()
        for v in range(N):
            if V[v] == 0 and G[u][v] > 0:
                Q.append(v)
                P[v]  = u
                V[v] += 1

    return V[T] == 1


def floyd_fulkerson(G, S, T, N):
    P = [0 for _ in range(N)]
    M = 0

    while breadth_first_search(G, P, S, T, N):
        F = 999999

        v = T
        while v != S:
            u = P[v]
            F = min(F, G[u][v])
            v = P[v]

        v = T
        while v != S:
            u        = P[v]
            G[u][v] -= F
            G[v][u] += F
            v        = P[v]

        M += F

    return M


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    C     = lines[0][0]
    I     = 1

    for _ in range(C):
        N, T, M = lines[I]
        I      += 1

        E       = [[0 for _ in range((2 * N) + 2)] for _ in range((2 * N) + 2)]

        for a, b in lines[I:I + M]:
            E[(2 * a)][(2 * b) + 1] = 1
            E[(2 * b)][(2 * a) + 1] = 1

        for n in range(1, N + 1):
            E[0][(2 * n)]     = T
            E[(2 * n) + 1][1] = 1

        I      += M
        print(floyd_fulkerson(E, 0, 1, (2 * N) + 2))


if __name__ == "__main__":
    main(sys.argv[1:])

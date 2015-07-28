import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def cut_tree(G, N):
        D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

        def dfs(P, C):
            D[C][0] = 1

            for n in G[C]:

                if n != P:
                    dfs(C, n)

                    F = [0 for _ in range(N + 1)]
                    for j in range(N - 1, -1, -1):
                        F[j + 1] = D[C][j]
                    F[0] = 0

                    for j in range(N):
                        for k in range(N - j):
                            F[j + k] += D[C][j] * D[n][k]

                    for j in range(N):
                        D[C][j] = F[j]

                    for j in range(N - 1, -1, -1):
                        D[n][j + 1] = D[n][j]
                    D[n][0] = 0

        dfs(0, 1)

        return D


    def main():
        N, K = [int(i) for i in input().split()]

        G    = defaultdict(list)
        for _ in range(N - 1):
            x, y = [int(i) for i in input().split()]
            G[x].append(y)
            G[y].append(x)

        D    = cut_tree(G, N)

        R    = 1
        for i in range(1, N + 1):
            for j in range(K + 1):
                R += D[i][j]

        print(R)


    if __name__ == "__main__":
        main()

'''

def cut_tree(G, N):
    D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

    def dfs(P, C):
        D[C][0] = 1

        for n in G[C]:

            if n != P:
                dfs(C, n)

                F = [0 for _ in range(N + 1)]
                for j in range(N - 1, -1, -1):
                    F[j + 1] = D[C][j]
                F[0] = 0

                for j in range(N):
                    for k in range(N - j):
                        F[j + k] += D[C][j] * D[n][k]

                for j in range(N):
                    D[C][j] = F[j]

                for j in range(N - 1, -1, -1):
                    D[n][j + 1] = D[n][j]
                D[n][0] = 0

    dfs(0, 1)

    return D


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, K  = lines[0]

    G     = defaultdict(list)
    for x, y in lines[1:]:
        G[x].append(y)
        G[y].append(x)

    D     = cut_tree(G, N)

    R     = 1
    for i in range(1, N + 1):
        for j in range(K + 1):
            R += D[i][j]

    print(R)


if __name__ == "__main__":
    main(sys.argv[1:])

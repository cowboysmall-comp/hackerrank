import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def moves(N, M, X, D):
        W = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

        for i in range(N):
            T = [[0 for _ in range(M + 1)] for _ in range(D[i] + 1)]

            for j in range(1, D[i] + 1):
                T[j][0] = 1

            for j in range(1, M + 1):
                for k in range(1, D[i] + 1):
                    if k - 1 > 0:
                        T[k][j] += T[k - 1][j - 1]
                        T[k][j] %= 1000000007
                    if k + 1 <= D[i]:
                        T[k][j] += T[k + 1][j - 1]
                        T[k][j] %= 1000000007

            W[i + 1][0] = 1
            for j in range(1, M + 1):
                W[i + 1][j] = T[X[i]][j]

        return W


    def combs(M):
        C = [[0 for _ in range(M + 1)] for _ in range(M + 1)]

        for i in range(M + 1):
            C[i][0] = 1
            C[i][i] = 1

        for i in range(1, M + 1):
            for j in range(1, i):
                C[i][j]  = C[i - 1][j - 1] + C[i - 1][j]

        return C


    def ways(N, M, W, C):
        T = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

        for i in range(M + 1):
            T[1][i] = W[1][i]

        for i in range(N + 1):
            T[i][0] = 1

        for i in range(2, N + 1):
            for j in range(1, M + 1):
                T[i][j] = 0
                for k in range(j + 1):
                    T[i][j] += C[j][j - k] * W[i][j - k] * T[i - 1][k]
                    T[i][j] %= 1000000007

        return T[N][M]


    def main():
        T = int(input())

        for _ in range(T):
            N, M = [int(v) for v in input().split()]
            X    = [int(v) for v in input().split()]
            D    = [int(v) for v in input().split()]
            W    = moves(N, M, X, D)
            C    = combs(M)
            print(ways(N, M, W, C))


    if __name__ == "__main__":
        main()

'''

def moves(N, M, X, D):
    W = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(N):
        T = [[0 for _ in range(M + 1)] for _ in range(D[i] + 1)]

        for j in range(1, D[i] + 1):
            T[j][0] = 1

        for j in range(1, M + 1):
            for k in range(1, D[i] + 1):
                if k - 1 > 0:
                    T[k][j] += T[k - 1][j - 1]
                    T[k][j] %= 1000000007
                if k + 1 <= D[i]:
                    T[k][j] += T[k + 1][j - 1]
                    T[k][j] %= 1000000007

        W[i + 1][0] = 1
        for j in range(1, M + 1):
            W[i + 1][j] = T[X[i]][j]

    return W


def combs(M):
    C = [[0 for _ in range(M + 1)] for _ in range(M + 1)]

    for i in range(M + 1):
        C[i][0] = 1
        C[i][i] = 1

    for i in range(1, M + 1):
        for j in range(1, i):
            C[i][j]  = C[i - 1][j - 1] + C[i - 1][j]
            C[i][j] %= 1000000007

    return C


def ways(N, M, W, C):
    T = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(M + 1):
        T[1][i] = W[1][i]

    for i in range(N + 1):
        T[i][0] = 1

    for i in range(2, N + 1):
        for j in range(1, M + 1):
            T[i][j] = 0
            for k in range(j + 1):
                T[i][j] += C[j][j - k] * W[i][j - k] * T[i - 1][k]
                T[i][j] %= 1000000007

    return T[N][M]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N, M = lines[(3 * i) + 1]
        X    = lines[(3 * i) + 2]
        D    = lines[(3 * i) + 3]
        W    = moves(N, M, X, D)
        C    = combs(M)
        print(ways(N, M, W, C))


if __name__ == "__main__":
    main(sys.argv[1:])

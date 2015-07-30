import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def coin_on_the_table(N, M, K, B):
        C          = [[[999999 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
        C[0][0][0] = 0

        for k in range(1, K + 1):
            for i in range(N):
                for j in range(M):
                    if i > 0:
                        C[i][j][k] = min(C[i][j][k], C[i - 1][j][k - 1] + (B[i - 1][j] != 'D'))
                    if i < N - 1:
                        C[i][j][k] = min(C[i][j][k], C[i + 1][j][k - 1] + (B[i + 1][j] != 'U'))
                    if j > 0:
                        C[i][j][k] = min(C[i][j][k], C[i][j - 1][k - 1] + (B[i][j - 1] != 'R'))
                    if j < M - 1:
                        C[i][j][k] = min(C[i][j][k], C[i][j + 1][k - 1] + (B[i][j + 1] != 'L'))

        for i in range(N):
            for j in range(M):
                if B[i][j] == '*':
                    return min(C[i][j])

        return None


    def main():
        N, M, K = [int(i) for i in input().split()]
        B       = [input() for _ in range(N)]
        C       = coin_on_the_table(N, M, K, B)

        print(-1 if C == 999999 else C)


    if __name__ == "__main__":
        main()


    recursive solution - much faster than the DP solution:

    def coin_on_the_table(N, M, K, B):
        C = [[999999 for _ in range(M)] for _ in range(N)]

        def search(i, j, S, T):
            if 0 <= i < N and 0 <= j < M and S <= K and T < C[i][j]:
                C[i][j] = T
                search(i + 1, j, S + 1, T + (B[i][j] != 'D'))
                search(i - 1, j, S + 1, T + (B[i][j] != 'U'))
                search(i, j + 1, S + 1, T + (B[i][j] != 'R'))
                search(i, j - 1, S + 1, T + (B[i][j] != 'L'))

        search(0, 0, 0, 0)

        for i in range(N):
            for j in range(M):
                if B[i][j] == '*':
                    return C[i][j]

        return None

'''

def coin_on_the_table(N, M, K, B):
    C          = [[[999999 for _ in range(K + 1)] for _ in range(M)] for _ in range(N)]
    C[0][0][0] = 0

    for k in range(1, K + 1):
        for i in range(N):
            for j in range(M):
                if i > 0:
                    C[i][j][k] = min(C[i][j][k], C[i - 1][j][k - 1] + (B[i - 1][j] != 'D'))
                if i < N - 1:
                    C[i][j][k] = min(C[i][j][k], C[i + 1][j][k - 1] + (B[i + 1][j] != 'U'))
                if j > 0:
                    C[i][j][k] = min(C[i][j][k], C[i][j - 1][k - 1] + (B[i][j - 1] != 'R'))
                if j < M - 1:
                    C[i][j][k] = min(C[i][j][k], C[i][j + 1][k - 1] + (B[i][j + 1] != 'L'))

    for i in range(N):
        for j in range(M):
            if B[i][j] == '*':
                return min(C[i][j])

    return None


def main(argv):
    lines   = files.read_lines(argv[0])
    N, M, K = [int(i) for i in lines[0].split()]
    B       = lines[1:]
    C       = coin_on_the_table(N, M, K, B)

    print(-1 if C == 999999 else C)


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def perimeter(M, N, A):
        B = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
        C = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

        for i in range(M):
            B[i][N] = N

        for i in range(N):
            C[M][i] = M

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                B[i][j] = j if A[i][j] == 'x' else B[i][j + 1]
                C[i][j] = i if A[i][j] == 'x' else C[i + 1][j]

        R = 0
        for i in range(M):
            for j in range(N):
                if A[i][j] == '.':
                    for k in range(j + 1, B[i][j]):
                        for l in range(i + 1, min(C[i][j], C[i][k])):
                            if B[l][j] > k:
                                R = max(R, 2 * (l - i) + 2 * (k - j))

        return R


    def main():
        M, N = [int(i) for i in input().split()]
        A    = [input() for _ in range(M)]
        R    = perimeter(M, N, A)
        print(R if R > 0 else 'impossible')


    if __name__ == "__main__":
        main()

'''

def perimeter(M, N, A):
    B = [[0 for _ in range(N + 1)] for _ in range(M + 1)]
    C = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

    for i in range(M):
        B[i][N] = N

    for i in range(N):
        C[M][i] = M

    for i in range(M - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            B[i][j] = j if A[i][j] == 'x' else B[i][j + 1]
            C[i][j] = i if A[i][j] == 'x' else C[i + 1][j]

    R = 0
    for i in range(M):
        for j in range(N):
            if A[i][j] == '.':
                for k in range(j + 1, B[i][j]):
                    for l in range(i + 1, min(C[i][j], C[i][k])):
                        if B[l][j] > k:
                            R = max(R, 2 * (l - i) + 2 * (k - j))

    return R


def main(argv):
    lines = files.read_lines(argv[0])
    M, N  = [int(i) for i in lines[0].split()]
    A     = lines[1:]
    R     = perimeter(M, N, A)
    print(R if R > 0 else 'impossible')


if __name__ == "__main__":
    main(sys.argv[1:])

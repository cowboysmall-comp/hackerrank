import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def longest_common_subsequence(N, M, A, B):
        C = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
        S = []

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if A[i - 1] == B[j - 1]:
                    C[i][j] = C[i - 1][j - 1] + 1
                else:
                    C[i][j] = max(C[i][j - 1], C[i - 1][j])

        while N != 0 and M != 0:
            if C[N][M] == C[N - 1][M]:
                N -= 1
            elif C[N][M] == C[N][M - 1]:
                M -= 1
            elif A[N - 1] == B[M - 1]:
                S.insert(0, A[N - 1])
                N -= 1
                M -= 1

        return ' '.join(str(s) for s in S)


    def main():
        N, M = [int(i) for i in input().split()]
        A    = [int(i) for i in input().split()]
        B    = [int(i) for i in input().split()]

        print(longest_common_subsequence(N, M, A, B))


    if __name__ == "__main__":
        main()

'''

def longest_common_subsequence(N, M, A, B):
    C = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    S = []

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])

    while N != 0 and M != 0:
        if C[N][M] == C[N - 1][M]:
            N -= 1
        elif C[N][M] == C[N][M - 1]:
            M -= 1
        elif A[N - 1] == B[M - 1]:
            S.insert(0, A[N - 1])
            N -= 1
            M -= 1

    return ' '.join(str(s) for s in S)


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, M  = lines[0]
    A     = lines[1]
    B     = lines[2]

    print(longest_common_subsequence(N, M, A, B))


if __name__ == "__main__":
    main(sys.argv[1:])

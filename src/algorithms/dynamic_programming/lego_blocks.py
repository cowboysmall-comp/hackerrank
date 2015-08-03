import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def lego_blocks(N, M):
        F    = [0 for _ in range(M + 1)]
        G    = [0 for _ in range(M + 1)]
        S    = [0 for _ in range(M + 1)]

        for i in range(M + 1):
            F[i] += 1 if i == 0 else pow(2, i - 1) if 0 < i < 4 else (F[i - 1] + F[i - 2] + F[i - 3] + F[i - 4])
            F[i] %= 1000000007

            G[i]  = pow(F[i], N, 1000000007)

            S[i] = G[i]
            for j in range(1, i):
                S[i] -= S[j] * G[i - j]
                S[i] %= 1000000007

        return S[M]


    def main():
        T = int(input())

        for _ in range(T):
            N, M = [int(i) for i in input().split()]
            print(lego_blocks(N, M))


    if __name__ == "__main__":
        main()

'''

def lego_blocks(N, M):
    F    = [0 for _ in range(M + 1)]
    G    = [0 for _ in range(M + 1)]
    S    = [0 for _ in range(M + 1)]

    for i in range(M + 1):
        F[i] += 1 if i == 0 else pow(2, i - 1) if 0 < i < 4 else (F[i - 1] + F[i - 2] + F[i - 3] + F[i - 4])
        F[i] %= 1000000007

        G[i]  = pow(F[i], N, 1000000007)

        S[i] = G[i]
        for j in range(1, i):
            S[i] -= S[j] * G[i - j]
            S[i] %= 1000000007

    return S[M]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N, M = lines[i + 1]
        print(lego_blocks(N, M))


if __name__ == "__main__":
    main(sys.argv[1:])

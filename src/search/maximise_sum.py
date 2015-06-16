import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

import bisect


'''
    submitted code:

    def maximise_sum(A, N, M):
        B = [0, M]

        S = 0
        V = 0

        for i in range(N):
            V += A[i]
            V %= M

            j = bisect.bisect(B, V)
            S = max(S, (V - B[j] + M) % M)

            B.insert(j, V)

        return S


    def main():
        T = int(input())

        for _ in range(T):
            N, M = [int(i) for i in input().split()]
            A    = [int(i) for i in input().split()]
            print(maximise_sum(A, N, M))


    if __name__ == "__main__":
        main()

'''

def maximise_sum(A, N, M):
    B = [0, M]

    S = 0
    V = 0

    for i in range(N):
        V += A[i]
        V %= M

        # the case of P[j] = 0, max(S, V) is
        # unnecessary, because of the presence 
        # of M in B - i.e. M % M == 0
        # so it is handled automatically
        # S = max(S, V)

        j  = bisect.bisect(B, V)
        S  = max(S, (V - B[j] + M) % M)

        B.insert(j, V)

    return S


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N, M = lines[(2 * i) + 1]
        A    = lines[(2 * i) + 2]
        print(maximise_sum(A, N, M))


if __name__ == "__main__":
    main(sys.argv[1:])

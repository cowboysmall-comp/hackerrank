import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def lis(N, A):
        T = [0 for _ in range(N)]
        P = [0 for _ in range(N)]
        L = 1

        def get_ceil_index(L, R, K):
            while R - L > 1:
                M = L + ((R - L) // 2)
                if A[T[M]] >= K:
                    R = M
                else:
                    L = M
            return R

        for i in range(1, N):
            if A[i] < A[T[0]]:
                T[0] = i
            elif A[i] > A[T[L - 1]]:
                T[L] = i
                L   += 1
            else:
                p    = get_ceil_index(-1, L - 1, A[i])
                P[i] = T[p - 1]
                T[p] = i

        return L


    def main():
        N = int(input())
        R = [int(input()) for _ in range(N)]

        print(lis(N, A))


    if __name__ == "__main__":
        main()

'''

def lis(N, A):
    T = [0 for _ in range(N)]
    P = [0 for _ in range(N)]
    L = 1

    def get_ceil_index(L, R, K):
        while R - L > 1:
            M = L + ((R - L) // 2)
            if A[T[M]] >= K:
                R = M
            else:
                L = M
        return R

    for i in range(1, N):
        if A[i] < A[T[0]]:
            T[0] = i
        elif A[i] > A[T[L - 1]]:
            T[L] = i
            L   += 1
        else:
            p    = get_ceil_index(-1, L - 1, A[i])
            P[i] = T[p - 1]
            T[p] = i

    return L


def main(argv):
    lines = files.read_ints(argv[0])
    N     = lines[0]
    A     = lines[1:]

    print(lis(N, A))


if __name__ == "__main__":
    main(sys.argv[1:])

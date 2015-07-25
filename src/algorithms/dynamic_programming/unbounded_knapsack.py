import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def knapsack(N, K, A):
        B = [0 for _ in range(K + 1)]
        M = min(A)

        for i in range(M, K + 1):
            B[i] = B[i - 1]
            for j in range(N):
                if A[j] <= i:
                    B[i] = max(B[i], B[i - A[j]] + A[j])

        return B[K]


    def main():
        T = int(input())

        for _ in range(T):
            N, K = [int(i) for i in input().split()]
            A    = [int(i) for i in input().split()]
            print(knapsack(N, K, A))


    if __name__ == "__main__":
        main()

'''

def knapsack(N, K, A):
    B = [0 for _ in range(K + 1)]
    M = min(A)

    for i in range(M, K + 1):
        B[i] = B[i - 1]
        for j in range(N):
            if A[j] <= i:
                B[i] = max(B[i], B[i - A[j]] + A[j])

    return B[K]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N, K = lines[(2 * i) + 1]
        A    = lines[(2 * i) + 2]
        print(knapsack(N, K, A))


if __name__ == "__main__":
    main(sys.argv[1:])

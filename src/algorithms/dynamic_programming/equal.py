import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def operations(N, A):
        M = min(A)
        S = max(0, M - 4)
        O = []

        for m in range(S, M + 1):
            C = 0
            for i in range(N):
                T  = A[i] - m
                C += T // 5 + (T % 5) // 2 + (T % 5) % 2
            O.append(C)

        return min(O)


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            A = [int(i) for i in input().split()]
            print(operations(N, A))


    if __name__ == "__main__":
        main()

'''

def operations(N, A):
    M = min(A)
    S = max(0, M - 4)
    O = []

    for m in range(S, M + 1):
        C = 0
        for i in range(N):
            T  = A[i] - m
            C += T // 5 + (T % 5) // 2 + (T % 5) % 2
        O.append(C)

    return min(O)


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N = lines[(2 * i) + 1][0]
        A = lines[(2 * i) + 2]
        print(operations(N, A))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

import bisect


'''
    submitted code:

    def maximize_sum(A, M):
        B = [0, M]

        S = 0
        V = 0

        for a in A:
            V += a
            V %= M

            i = bisect.bisect(B, V)
            S = max(S, (V - B[i] + M) % M)

            B.insert(i, V)

        return S


    def main():
        T = int(input())

        for _ in range(T):
            N, M = [int(i) for i in input().split()]
            A    = [int(i) for i in input().split()]
            print(maximize_sum(A, M))


    if __name__ == "__main__":
        main()

'''

def maximize_sum(A, M):
    B = [0, M]

    S = 0
    V = 0

    for a in A:
        V += a
        V %= M

        i = bisect.bisect(B, V)
        S = max(S, (V - B[i] + M) % M)

        B.insert(i, V)

    return S


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N, M = lines[(2 * i) + 1]
        A    = lines[(2 * i) + 2]
        print(maximize_sum(A, M))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from itertools import combinations


'''
    submitted code:

    def set_positions(V):
        C = [i for i in range(64)]
        P = []
        I = 0

        while V:
            if V & 1 != 0:
                P.append(I)
                C[I] = P[0]
            I  += 1
            V >>= 1

        return C


    def count_positions(V):
        C = 0

        for i, v in enumerate(V):
            if i == v:
                C += 1

        return C


    def combine_positions(V, W):
        return [min(V[i], W[i]) for i in range(64)]


    def sum_subsets(V, M):
        S = count_positions(M)

        for i, v in enumerate(V):
            S += sum_subsets(V[i + 1:], combine_positions(M, v))

        return S


    def main():
        N = int(input())
        D = [set_positions(int(i)) for i in input().split()]

        print(sum_subsets(D, [i for i in range(64)]))


    if __name__ == "__main__":
        main()

'''

def set_positions(V):
    C = [i for i in range(64)]
    P = []
    I = 0

    while V:
        if V & 1 != 0:
            P.append(I)
            C[I] = P[0]
        I  += 1
        V >>= 1

    return C


def count_positions(V):
    C = 0

    for i, v in enumerate(V):
        if i == v:
            C += 1

    return C


def combine_positions(V, W):
    return [min(V[i], W[i]) for i in range(64)]


def sum_subsets(V, M):
    S = count_positions(M)

    for i, v in enumerate(V):
        S += sum_subsets(V[i + 1:], combine_positions(M, v))

    return S


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    D     = [set_positions(d) for d in lines[1]]

    print(sum_subsets(D, [i for i in range(64)]))


if __name__ == "__main__":
    main(sys.argv[1:])

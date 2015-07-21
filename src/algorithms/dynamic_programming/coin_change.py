import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def coin_change(C, N, M):
        T    = [0 for _ in range(N + 1)]
        T[0] = 1

        for i in range(M):
            for j in range(C[i], N + 1):
                T[j] += T[j - C[i]]

        return T[N]


    def main():
        N, M = [int(i) for i in input().split()]
        C    = [int(i) for i in input().split()]

        print(coin_change(C, N, M))


    if __name__ == "__main__":
        main()

'''

def coin_change(C, N, M):
    T    = [0 for _ in range(N + 1)]
    T[0] = 1

    for i in range(M):
        for j in range(C[i], N + 1):
            T[j] += T[j - C[i]]

    return T[N]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, M  = lines[0]
    C     = lines[1]

    print(coin_change(C, N, M))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files

import math


'''
    submitted code:

    def sieve(M):
        P = [True for _ in range(M + 1)]

        for i in range(2, int(math.sqrt(M)) + 1):
            if P[i]:
                for j in range(i ** 2, M + 1, i):
                    P[j] = False

        return len([i for i in range(2, M + 1) if P[i]])


    def count(N):
        C = [1 for _ in range(N + 1)]

        for i in range(4, N + 1):
            C[i] = C[i - 1] + C[i - 4]

        return C[N]


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            print(sieve(count(N)))


    if __name__ == "__main__":
        main()

'''

def sieve(M):
    P = [True for _ in range(M + 1)]

    for i in range(2, int(math.sqrt(M)) + 1):
        if P[i]:
            for j in range(i ** 2, M + 1, i):
                P[j] = False

    return len([i for i in range(2, M + 1) if P[i]])


def count(N):
    C = [1 for _ in range(N + 1)]

    for i in range(4, N + 1):
        C[i] = C[i - 1] + C[i - 4]

    return C[N]


def main(argv):
    lines = files.read_ints(argv[0])
    T     = lines[0]

    for i in range(T):
        N = lines[i + 1]
        print(sieve(count(N)))


if __name__ == "__main__":
    main(sys.argv[1:])

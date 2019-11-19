import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def stockmax(N, P):
        A = [0 for _ in range(N)]

        M = 0
        for n in range(N - 1, -1, -1):
            M    = max(M, P[n])
            A[n] = M

        T = 0
        for n in range(N):
            T += A[n] - P[n]

        return T


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            P = [int(i) for i in input().split()]
            print(stockmax(N, P))


    if __name__ == "__main__":
        main()

'''

def stockmax(N, P):
    A = [0 for _ in range(N)]

    M = 0
    for n in range(N - 1, -1, -1):
        M    = max(M, P[n])
        A[n] = M

    T = 0
    for n in range(N):
        T += A[n] - P[n]

    return T


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N = lines[(2 * i) + 1][0]
        X = lines[(2 * i) + 2]
        print(stockmax(N, X))


if __name__ == "__main__":
    main(sys.argv[1:])

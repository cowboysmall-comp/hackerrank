import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def bricks_game(N, A):
        P    = [0 for _ in range(N)]
        D    = [0 for _ in range(N)]

        P[0] = A[0]

        for i in range(1, N):
            P[i] = P[i - 1] + A[i]

        for i in range(3):
            D[i] = P[i]

        for i in range(3, N):
            X    = P[i - 1] + A[i] - D[i - 1]
            Y    = P[i - 2] + A[i] + A[i - 1] - D[i - 2]
            Z    = P[i - 3] + A[i] + A[i - 1] + A[i - 2] - D[i - 3]
            D[i] = max(X, Y, Z)

        return D[-1]


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            A = [int(i) for i in input().split()]
            print(bricks_game(N, A[::-1]))


    if __name__ == "__main__":
        main()

'''

def bricks_game(N, A):
    P    = [0 for _ in range(N)]
    D    = [0 for _ in range(N)]

    P[0] = A[0]

    for i in range(1, N):
        P[i] = P[i - 1] + A[i]

    for i in range(3):
        D[i] = P[i]

    for i in range(3, N):
        X    = P[i - 1] + A[i] - D[i - 1]
        Y    = P[i - 2] + A[i] + A[i - 1] - D[i - 2]
        Z    = P[i - 3] + A[i] + A[i - 1] + A[i - 2] - D[i - 3]
        D[i] = max(X, Y, Z)

    return D[-1]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N = lines[(2 * i) + 1][0]
        A = lines[(2 * i) + 2]
        print(bricks_game(N, A[::-1]))


if __name__ == "__main__":
    main(sys.argv[1:])

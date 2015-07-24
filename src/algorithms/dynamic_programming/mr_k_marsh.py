import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def perimeter(M, N, A):
        R = [0]
        B = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                B[i][j] += B[i][j - 1] + (A[i - 1][j - 1] == 'x')

        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                c = -1
                for k in range(1, M + 1):
                    if B[k][j] - B[k][i - 1] == 0:
                        if c == -1:
                            c = k
                        else:
                            R.append(2 * (j - i) + 2 * (k - c))
                    elif A[k - 1][i - 1] == 'x' or A[k - 1][j - 1] == 'x':
                        c = -1

        return max(R)


    def main():
        M, N = [int(i) for i in input().split()]
        A    = [[c for c in input()] for _ in range(M)]
        R    = perimeter(M, N, A)
        print(R if R > 0 else 'impossible')


    if __name__ == "__main__":
        main()

'''

def perimeter(M, N, A):
    R = [0]
    B = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

    V = False
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if not V and A[i - 1][j - 1] == 'x':
                V = True
            B[i][j] += B[i][j - 1] + (A[i - 1][j - 1] == 'x')

    if V:
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                c = -1
                for k in range(1, M + 1):
                    if B[k][j] - B[k][i - 1] == 0:
                        if c == -1:
                            c = k
                        else:
                            R.append(2 * (j - i) + 2 * (k - c))
                    elif A[k - 1][i - 1] == 'x' or A[k - 1][j - 1] == 'x':
                        c = -1

    return max(R)


def main(argv):
    lines = files.read_lines(argv[0])
    M, N  = [int(i) for i in lines[0].split()]
    A     = [[c for c in line] for line in lines[1:]]
    R     = perimeter(M, N, A)
    print(R if R > 0 else 'impossible')


if __name__ == "__main__":
    main(sys.argv[1:])

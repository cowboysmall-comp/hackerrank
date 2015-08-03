import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def diagonal_difference(A, N):
        return abs(sum(A[i][i] for i in range(N)) - sum(A[i][N - i - 1] for i in range(N)))


    def main():
        N = int(input())
        A = [[int(i) for i in input().split()] for _ in range(N)]

        print(diagonal_difference(A, N))


    if __name__ == "__main__":
        main()

'''

def diagonal_difference(A, N):
    return abs(sum(A[i][i] for i in range(N)) - sum(A[i][N - i - 1] for i in range(N)))


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    A     = lines[1:]

    print(diagonal_difference(A, N))


if __name__ == "__main__":
    main(sys.argv[1:])

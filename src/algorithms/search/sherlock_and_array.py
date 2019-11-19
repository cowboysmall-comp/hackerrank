import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def divisible(N, A):
        S = [0 for _ in range(N + 2)]

        for i in range(N):
            S[i + 1] = S[i] + A[i]

        for i in range(N):
            if S[i] == S[-2] - S[i + 1]:
                return True

        return False


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            A = [int(i) for i in input().split()]
            print('YES' if divisible(N, A) else 'NO')


    if __name__ == "__main__":
        main()

'''


def divisible(N, A):
    S = [0 for _ in range(N + 2)]

    for i in range(N):
        S[i + 1] = S[i] + A[i]

    for i in range(N):
        if S[i] == S[-2] - S[i + 1]:
            return True

    return False


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N = lines[(2 * i) + 1][0]
        A = lines[(2 * i) + 2]
        print('YES' if divisible(N, A) else 'NO')


if __name__ == "__main__":
    main(sys.argv[1:])

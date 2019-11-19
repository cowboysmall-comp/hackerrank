import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def two_sum(M, N, C):
        indices = {}

        for i in range(N):
            rem = M - C[i]
            if rem in indices:
                return indices[rem] + 1, i + 1
            else:
                indices[C[i]] = i

        return 0, 0


    def main():
        T = int(input())

        for _ in range(T):
            M = int(input())
            N = int(input())
            C = [int(i) for i in input().split()]
            print(' '.join(str(i) for i in two_sum(M, N, C)))


    if __name__ == "__main__":
        main()

'''


def two_sum(M, N, C):
    indices = {}

    for i in range(N):
        rem = M - C[i]
        if rem in indices:
            return indices[rem] + 1, i + 1
        else:
            indices[C[i]] = i

    return 0, 0


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        M = lines[(3 * i) + 1][0]
        N = lines[(3 * i) + 2][0]
        C = lines[(3 * i) + 3]
        print(' '.join(str(i) for i in two_sum(M, N, C)))


if __name__ == "__main__":
    main(sys.argv[1:])

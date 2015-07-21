import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def candies(N, R):
        C = [1 for _ in range(N)]

        for i in range(1, N):
            if R[i] > R[i - 1] and C[i] <= C[i - 1]:
                C[i] = max(C[i - 1] + 1, C[i])

        for i in range(N - 2, -1, -1):
            if R[i] > R[i + 1] and C[i] <= C[i + 1]:
                C[i] = max(C[i + 1] + 1, C[i])

        return sum(C)


    def main():
        N = int(input())
        R = [int(input()) for _ in range(N)]

        print(candies(N, R))


    if __name__ == "__main__":
        main()

'''

def candies(N, R):
    C = [1 for _ in range(N)]

    for i in range(1, N):
        if R[i] > R[i - 1] and C[i] <= C[i - 1]:
            C[i] = max(C[i - 1] + 1, C[i])

    for i in range(N - 2, -1, -1):
        if R[i] > R[i + 1] and C[i] <= C[i + 1]:
            C[i] = max(C[i + 1] + 1, C[i])

    return sum(C)


def main(argv):
    lines = files.read_ints(argv[0])
    N     = lines[0]
    R     = lines[1:]

    print(candies(N, R))


if __name__ == "__main__":
    main(sys.argv[1:])

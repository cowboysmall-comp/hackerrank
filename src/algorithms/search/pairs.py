import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

import bisect


'''
    submitted code:

    def pairs(A, N, K):
        pairs = []

        for a in A:
            i = bisect.bisect_left(A, a + K)
            if 0 < i < N and A[i] - a == K:
                pairs.append((a, a + K))

        return len(pairs)


    def main():
        N, K = [int(i) for i in input().split()]
        A    = [int(i) for i in input().split()]

        print(pairs(sorted(A), N, K))


    if __name__ == "__main__":
        main()

'''

def pairs(A, N, K):
    pairs = []

    for a in A:
        i = bisect.bisect_left(A, a + K)
        if 0 < i < N and A[i] - a == K:
            pairs.append((a, a + K))

    return len(pairs)


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    N, K = lines[0]
    A    = lines[1]

    print(pairs(sorted(A), N, K))


if __name__ == "__main__":
    main(sys.argv[1:])

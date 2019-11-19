import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def closest_numbers(A):
        pairs = defaultdict(list)

        for i in range(1, len(A)):
            pairs[A[i] - A[i - 1]].append((A[i - 1], A[i]))

        return pairs[min(pairs)]


    def main():
        N = int(input())
        A = [int(i) for i in input().split()]

        print(' '.join(['%s %s' % (vals[0], vals[1]) for vals in closest_numbers(sorted(A))]))


    if __name__ == "__main__":
        main()

'''

def closest_numbers(A):
    pairs = defaultdict(list)

    for i in range(1, len(A)):
        pairs[A[i] - A[i - 1]].append((A[i - 1], A[i]))

    return pairs[min(pairs)]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    A     = lines[1]

    print(' '.join(['%s %s' % (vals[0], vals[1]) for vals in closest_numbers(sorted(A))]))


if __name__ == "__main__":
    main(sys.argv[1:])

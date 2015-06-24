import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def missing_numbers(A, B):
        count = defaultdict(int)

        for b in B:
            count[b] += 1

        for a in A:
            count[a] -= 1

        return sorted([key for key in count if count[key] > 0])


    def main():
        n = int(input())
        A = [int(i) for i in input().split()]
        m = int(input())
        B = [int(i) for i in input().split()]

        print(' '.join(str(val) for val in missing_numbers(A, B)))


    if __name__ == "__main__":
        main()

'''


def missing_numbers(A, B):
    count = defaultdict(int)

    for b in B:
        count[b] += 1

    for a in A:
        count[a] -= 1

    return sorted([key for key in count if count[key] > 0])



def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    A     = lines[1]
    B     = lines[3]

    print(' '.join(str(val) for val in missing_numbers(A, B)))


if __name__ == "__main__":
    main(sys.argv[1:])

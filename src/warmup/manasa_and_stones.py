import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code:

    def last_stones(n, a, b):
        totals = set()

        for i in range(n):
            totals.add(((n - 1 - i) * a) + (i * b))

        return totals


    def main():
        T     = int(input())

        for i in range(T):
            n = int(input())
            a = int(input())
            b = int(input())
            print(' '.join(str(val) for val in sorted(last_stones(n, a, b))))


    if __name__ == "__main__":
        main()

'''


def last_stones(n, a, b):
    totals = set()

    for i in range(n):
        totals.add(((n - 1 - i) * a) + (i * b))

    return totals


def main(argv):
    lines = files.read_ints(argv[0])
    T     = lines[0]

    for i in range(T):
        n = lines[(3 * i) + 1]
        a = lines[(3 * i) + 2]
        b = lines[(3 * i) + 3]
        print(' '.join(str(val) for val in sorted(last_stones(n, a, b))))


if __name__ == "__main__":
    main(sys.argv[1:])

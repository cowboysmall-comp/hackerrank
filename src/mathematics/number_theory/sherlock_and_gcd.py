import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files

from functools import reduce


'''
    submitted code:

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a


    def gcd_multiple(numbers):
        return reduce(gcd, numbers)


    def main():
        T = int(input())

        for i in range(T):
            input()
            if gcd_multiple(set([int(val) for val in input().split()])) == 1:
                print('YES')
            else:
                print('NO')


    if __name__ == "__main__":
        main()

'''

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_multiple(numbers):
    return reduce(gcd, numbers)


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        if gcd_multiple(set(lines[(2 * i) + 2])) == 1:
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    main(sys.argv[1:])

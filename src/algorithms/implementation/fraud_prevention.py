import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def parse_email(E):
        E    = E.lower()
        B, A = E.split('@')

        if '.' in B:
            B = ''.join(B.split('.'))
        if '+' in B:
            B = B[:B.find('+')]

        return B + '@' + A


    def parse_address(A):
        A = [a.lower() for a in A]

        if 'street' in A[0]:
            A[0] = A[0][:A[0].find('street')] + 'st.'

        if 'road' in A[0]:
            A[0] = A[0][:A[0].find('road')] + 'rd.'

        if 'california' in A[2]:
            A[2] = A[2][:A[2].find('california')] + 'ca'

        if 'illinois' in A[2]:
            A[2] = A[2][:A[2].find('illinois')] + 'il'

        if 'new york' in A[2]:
            A[2] = A[2][:A[2].find('new york')] + 'ny'

        if '-' in A[3]:
            A[3] = ''.join(A[3].split('-'))

        return '|'.join(A)


    def parse_record(R):
        return (int(R[0]), int(R[1]), parse_email(R[2]), parse_address(R[3:7]), R[7])


    def fraud_prevention(R):
        C = defaultdict(set)

        for r in R:
            c = (r[2], r[1])
            if c not in C or filter(lambda x: x[4] != r[4], C[c]):
                C[c].add(r)

            c = (r[3], r[1])
            if c not in C or filter(lambda x: x[4] != r[4], C[c]):
                C[c].add(r)

        return sorted(c[0] for c in set.union(*filter(lambda x: len(x) > 1, C.values())))


    def main():
        N = int(input())
        R = [parse_record(input().split(',')) for _ in range(N)]

        print(','.join(str(f) for f in fraud_prevention(R)))


    if __name__ == "__main__":
        main()

'''


def parse_email(E):
    E    = E.lower()
    B, A = E.split('@')

    if '.' in B:
        B = ''.join(B.split('.'))
    if '+' in B:
        B = B[:B.find('+')]

    return B + '@' + A


def parse_address(A):
    A = [a.lower() for a in A]

    if 'street' in A[0]:
        A[0] = A[0][:A[0].find('street')] + 'st.'

    if 'road' in A[0]:
        A[0] = A[0][:A[0].find('road')] + 'rd.'

    if 'california' in A[2]:
        A[2] = A[2][:A[2].find('california')] + 'ca'

    if 'illinois' in A[2]:
        A[2] = A[2][:A[2].find('illinois')] + 'il'

    if 'new york' in A[2]:
        A[2] = A[2][:A[2].find('new york')] + 'ny'

    if '-' in A[3]:
        A[3] = ''.join(A[3].split('-'))

    return '|'.join(A)


def parse_record(R):
    return (int(R[0]), int(R[1]), parse_email(R[2]), parse_address(R[3:7]), R[7])


def fraud_prevention(R):
    C = defaultdict(set)

    for r in R:
        c = (r[2], r[1])
        if c not in C or filter(lambda x: x[4] != r[4], C[c]):
            C[c].add(r)

        c = (r[3], r[1])
        if c not in C or filter(lambda x: x[4] != r[4], C[c]):
            C[c].add(r)

    return sorted(c[0] for c in set.union(*filter(lambda x: len(x) > 1, C.values())))


def main(argv):
    lines = files.read_lines(argv[0])
    N     = int(lines[0])
    R     = [parse_record(line.split(',')) for line in lines[1:]]

    print(','.join(str(f) for f in fraud_prevention(R)))


if __name__ == "__main__":
    main(sys.argv[1:])

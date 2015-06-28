import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def symmetric_point(P, Q):
        return ((2 * Q[0]) - P[0], (2 * Q[1]) - P[1])


    def main():
        T = int(input())

        for _ in range(T):
            P1, P2, Q1, Q2 = [int(i) for i in input().split()]
            print('%s %s' % symmetric_point((P1, P2), (Q1, Q2)))


    if __name__ == "__main__":
        main()

'''


def symmetric_point(P, Q):
    return ((2 * Q[0]) - P[0], (2 * Q[1]) - P[1])


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for P1, P2, Q1, Q2 in lines[1:]:
        print('%s %s' % symmetric_point((P1, P2), (Q1, Q2)))


if __name__ == "__main__":
    main(sys.argv[1:])

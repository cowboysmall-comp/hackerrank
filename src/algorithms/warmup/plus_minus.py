import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def plus_minus(A):
        length   = len(A)
        positive = len([a for a in A if a > 0]) / length
        negative = len([a for a in A if a < 0]) / length
        zero     = len([a for a in A if a == 0]) / length
        return positive, negative, zero


    def main():
        N = int(input())
        A = [int(i) for i in input().split()]

        print('\n'.join('%0.6f' % v for v in plus_minus(A)))


    if __name__ == "__main__":
        main()

'''

def plus_minus(A):
    length   = len(A)
    positive = len([a for a in A if a > 0]) / length
    negative = len([a for a in A if a < 0]) / length
    zero     = len([a for a in A if a == 0]) / length
    return positive, negative, zero


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    A     = lines[1]

    print('\n'.join('%0.6f' % v for v in plus_minus(A)))


if __name__ == "__main__":
    main(sys.argv[1:])

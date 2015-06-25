import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def staircase(N):
        S = []

        for i in range(N):
            R = ''
            for j in range(N):
                if N - i - 1 <= j:
                    R += '#'
                else:
                    R += ' '
            S.append(R)

        return S


    def main():
        N = int(input())

        print('\n'.join('%s' % row for row in staircase(N)))


    if __name__ == "__main__":
        main()

'''


def staircase(N):
    S = []

    for i in range(N):
        R = ''
        for j in range(N):
            if N - i - 1 <= j:
                R += '#'
            else:
                R += ' '
        S.append(R)

    return S


def main(argv):
    N = files.read_int(argv[0])

    print('\n'.join('%s' % row for row in staircase(N)))


if __name__ == "__main__":
    main(sys.argv[1:])

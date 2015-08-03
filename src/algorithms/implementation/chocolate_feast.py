import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def chocolate_feast(N, C, M):
        wrappers = N // C
        count    = wrappers

        while wrappers >= M:
            free      = wrappers // M
            remaining = wrappers  % M
            count    += free

            wrappers  = free + remaining

        return count


    def main():
        T = int(input())

        for _ in range(T):
            N, C, M = [int(val) for val in input().split()]
            print(chocolate_feast(N, C, M))


    if __name__ == "__main__":
        main()

'''

def chocolate_feast(N, C, M):
    wrappers = N // C
    count    = wrappers

    while wrappers >= M:
        free      = wrappers // M
        remaining = wrappers  % M
        count    += free

        wrappers  = free + remaining

    return count


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for line in lines[1:]:
        print(chocolate_feast(*line))


if __name__ == "__main__":
    main(sys.argv[1:])

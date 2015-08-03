import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def candles_counting(N, K, A):
        return -1


    def main():
        N, K = [int(i) for i in input().split()]
        A    = []
        for _ in range(N):
            A.append([int(i) for i in input().split()])

        print(candles_counting(N, K, A))


    if __name__ == "__main__":
        main()

'''

def candles_counting(N, K, A):
    return -1


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, K  = lines[0]
    A     = lines[1:]

    print(candles_counting(N, K, A))


if __name__ == "__main__":
    main(sys.argv[1:])

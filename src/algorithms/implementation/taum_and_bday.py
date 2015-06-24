import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def minimum_spend(B, W, X, Y, Z):
        return min((B * X) + (W * Y), (B * X) + (W * (X + Z)), (B * (Y + Z)) + (W * Y))


    def main():
        T = int(input())

        for i in range(T):
            B, W    = [int(val) for val in input().split()]
            X, Y, Z = [int(val) for val in input().split()]
            print(minimum_spend(B, W, X, Y, Z))


    if __name__ == "__main__":
        main()

'''


def minimum_spend(B, W, X, Y, Z):
    return min((B * X) + (W * Y), (B * X) + (W * (X + Z)), (B * (Y + Z)) + (W * Y))


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        B, W    = lines[(2 * i) + 1]
        X, Y, Z = lines[(2 * i) + 2]
        print(minimum_spend(B, W, X, Y, Z))


if __name__ == "__main__":
    main(sys.argv[1:])

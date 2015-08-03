import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def vertical_sticks(N, Y):
        return (N + 1) * sum(1 / (len([z for z in Y if z >= y]) + 1) for y in Y)


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            Y = [int(i) for i in input().split()]
            print('%0.2f' % vertical_sticks(N, Y))


    if __name__ == "__main__":
        main()

'''

def vertical_sticks(N, Y):
    return (N + 1) * sum(1 / (len([z for z in Y if z >= y]) + 1) for y in Y)


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N = lines[(2 * i) + 1][0]
        Y = lines[(2 * i) + 2]
        print('%0.2f' % vertical_sticks(N, Y))


if __name__ == "__main__":
    main(sys.argv[1:])

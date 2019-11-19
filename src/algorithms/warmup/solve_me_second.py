import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def solve_me_second(a, b):
        return a + b


    def main():
        n = int(input())

        for _ in range(n):
            a, b = [int(i) for i in input().split()]
            print(solve_me_second(a, b))


    if __name__ == "__main__":
        main()

'''

def solve_me_second(a, b):
    return a + b


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    n     = lines[0][0]

    for i in range(1, n + 1):
        a, b = lines[i]
        print(solve_me_second(a, b))


if __name__ == "__main__":
    main(sys.argv[1:])

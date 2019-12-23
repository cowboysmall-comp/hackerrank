import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def simple_array_sum(n, ar):
        return sum(ar)


    def main():
        n  = int(input())
        ar = [int(i) for i in input().split()]

        print(simple_array_sum(n, ar))


    if __name__ == "__main__":
        main()

'''

def simple_array_sum(ar):
    return sum(ar)


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    n     = lines[0][0]
    ar    = lines[1]

    print(simple_array_sum(ar))


if __name__ == "__main__":
    main(sys.argv[1:])

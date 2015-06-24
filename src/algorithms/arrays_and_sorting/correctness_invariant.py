import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def insertion_sort(l):
        for i in range(1, len(l)):
            j = i-1
            key = l[i]
            while (l[j] > key) and (j >= 0):
               l[j+1] = l[j]
               j -= 1
            l[j+1] = key


    m  = int(input().strip())
    ar = [int(i) for i in input().strip().split()]

    insertion_sort(ar)

    print(" ".join(map(str, ar)))


'''


def insertion_sort(l):
    for i in range(1, len(l)):
        j   = i - 1
        key = l[i]

        while (l[j] > key) and (j >= 0):
            l[j + 1] = l[j]
            j -= 1

        l[j + 1] = key


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    s     = lines[0][0]
    ar    = lines[1]

    insertion_sort(ar)

    print(' '.join(map(str, ar)))


if __name__ == "__main__":
    main(sys.argv[1:])

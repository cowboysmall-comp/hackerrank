import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code:

    def partition(array):
        return [val for val in array[1:] if val < array[0]] + [array[0]] + [val for val in array[1:] if val >= array[0]]


    def main():
        s  = int(input())
        ar = [int(i) for i in input().split()]

        print(' '.join(str(val) for val in partition(ar)))


    if __name__ == "__main__":
        main()


    alternative implementation:

    def partition(array):
        pivot   = array[0]
        less    = []
        greater = []

        for val in array[1:]:
            if val < pivot:
                less.append(val)
            else:
                greater.append(val)

        return less + [pivot] + greater

'''


def partition(array):
    return [val for val in array if val <= array[0]] + [val for val in array if val > array[0]]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    n     = lines[0][0]
    ar    = lines[1]

    print(' '.join(str(val) for val in partition(ar)))


if __name__ == "__main__":
    main(sys.argv[1:])

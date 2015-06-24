import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def insertion_sort(array):
        moves = []
        value = array[-1]
        i     = len(array) - 2

        while i >= 0 and array[i] > value:
            array[i + 1] = array[i]
            i -= 1
            moves.append(' '.join(str(val) for val in array))

        array[i + 1] = value
        moves.append(' '.join(str(val) for val in array))

        return moves


    def main():
        s  = int(input())
        ar = [int(i) for i in input().split()]

        print('\n'.join(insertion_sort(ar)))


    if __name__ == "__main__":
        main()

'''


def insertion_sort(array):
    moves = []
    value = array[-1]
    i     = len(array) - 2

    while i >= 0 and array[i] > value:
        array[i + 1] = array[i]
        i -= 1
        moves.append(' '.join(str(val) for val in array))

    array[i + 1] = value
    moves.append(' '.join(str(val) for val in array))

    return moves


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    s     = lines[0][0]
    ar    = lines[1]

    print('\n'.join(insertion_sort(ar)))


if __name__ == "__main__":
    main(sys.argv[1:])

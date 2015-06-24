import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def insertion_sort(array):
        shifts = 0

        for i in range(1, len(array)):
            j     = i - 1
            value = array[i]

            while j >= 0 and array[j] > value:
                array[j + 1] = array[j]
                j -= 1
                shifts += 1

            array[j + 1] = value

        return shifts


    def main():
        N  = int(input())
        ar = [int(i) for i in input().split()]

        print(insertion_sort(ar))


    if __name__ == "__main__":
        main()

'''


def insertion_sort(array):
    shifts = 0

    for i in range(1, len(array)):
        j     = i - 1
        value = array[i]

        while j >= 0 and array[j] > value:
            array[j + 1] = array[j]
            j -= 1
            shifts += 1

        array[j + 1] = value

    return shifts


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    ar    = lines[1]

    print(insertion_sort(ar))


if __name__ == "__main__":
    main(sys.argv[1:])

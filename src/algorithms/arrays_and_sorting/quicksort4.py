import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def partition(array, lower, upper):
        index = lower
        value = array[upper]
        swaps = 0

        for j in range(lower, upper):
            if array[j] <= value:
                array[j], array[index] = array[index], array[j]
                index += 1
                swaps += 1

        array[upper], array[index] = array[index], array[upper]
        swaps += 1

        return index, swaps


    def quick_sort(array, lower, higher):
        swaps = 0

        if lower < higher:
            p, s   = partition(array, lower, higher)

            swaps += s
            swaps += quick_sort(array, lower, p - 1)
            swaps += quick_sort(array, p + 1, higher)

        return swaps


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
        n      = int(input())
        ar     = [int(i) for i in input().split()]

        shifts = insertion_sort(ar[:])
        swaps  = quick_sort(ar, 0, n - 1)

        print(shifts - swaps)


    if __name__ == "__main__":
        main()

'''


def partition(array, lower, upper):
    index = lower
    value = array[upper]
    swaps = 0

    for j in range(lower, upper):
        if array[j] <= value:
            array[j], array[index] = array[index], array[j]
            index += 1
            swaps += 1

    array[upper], array[index] = array[index], array[upper]
    swaps += 1

    return index, swaps


def quick_sort(array, lower, higher):
    swaps = 0

    if lower < higher:
        p, s   = partition(array, lower, higher)

        swaps += s
        swaps += quick_sort(array, lower, p - 1)
        swaps += quick_sort(array, p + 1, higher)

    return swaps


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
    lines  = files.read_lines_of_ints(argv[0])
    n      = lines[0][0]
    ar     = lines[1]

    shifts = insertion_sort(ar[:])
    swaps  = quick_sort(ar, 0, n - 1)

    print(shifts - swaps)


if __name__ == "__main__":
    main(sys.argv[1:])

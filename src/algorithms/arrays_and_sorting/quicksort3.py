import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def partition(array, lower, upper):
        index = lower
        value = array[upper]

        for j in range(lower, upper):
            if array[j] <= value:
                array[j], array[index] = array[index], array[j]
                index += 1

        array[upper], array[index] = array[index], array[upper]

        return index


    def quick_sort(array, lower, higher, collector):
        if lower < higher:
            p = partition(array, lower, higher)

            collector.append(' '.join(str(val) for val in array))

            quick_sort(array, lower, p - 1, collector)
            quick_sort(array, p + 1, higher, collector)

        return array


    def main():
        n   = int(input())
        ar  = [int(i) for i in input().split()]

        col = []
        ar  = quick_sort(ar, 0, n - 1, col)

        print('\n'.join(str(val) for val in col))


    if __name__ == "__main__":
        main()

'''


def partition(array, lower, upper):
    index = lower
    value = array[upper]

    for j in range(lower, upper):
        if array[j] <= value:
            array[j], array[index] = array[index], array[j]
            index += 1

    array[upper], array[index] = array[index], array[upper]

    return index


def quick_sort(array, lower, higher, collector):
    if lower < higher:
        p = partition(array, lower, higher)

        collector.append(' '.join(str(val) for val in array))

        quick_sort(array, lower, p - 1, collector)
        quick_sort(array, p + 1, higher, collector)

    return array


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    n     = lines[0][0]
    ar    = lines[1]

    col   = []
    ar    = quick_sort(ar, 0, n - 1, col)

    print(' '.join(str(val) for val in ar))
    print()
    print('\n'.join(str(val) for val in col))


if __name__ == "__main__":
    main(sys.argv[1:])

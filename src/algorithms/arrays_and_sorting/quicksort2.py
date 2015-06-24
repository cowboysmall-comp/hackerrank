import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def partition(array, collector):
        if len(array) <= 1:
            return array
        else:
            less    = partition([val for val in array[1:] if val <= array[0]], collector)
            greater = partition([val for val in array[1:] if val > array[0]], collector)

            array   = less + [array[0]] + greater
            collector.append(' '.join(str(val) for val in array))

            return array


    def main():
        n   = int(input())
        ar  = [int(i) for i in input().split()]

        col = []
        ar  = partition(ar, col)

        print('\n'.join(str(val) for val in col))


    if __name__ == "__main__":
        main()


    alternative implementation:

    def partition(array, collector):
        if len(array) <= 1:
            return array
        else:
            pivot   = array[0]
            less    = []
            greater = []

            for val in array[1:]:
                if val < pivot:
                    less.append(val)
                else:
                    greater.append(val)

            array = partition(less, collector) + [pivot] + partition(greater, collector)
            collector.append(' '.join(str(val) for val in array))

            return array

'''


def partition(array, collector):
    if len(array) <= 1:
        return array
    else:
        less    = partition([val for val in array[1:] if val <= array[0]], collector)
        greater = partition([val for val in array[1:] if val > array[0]], collector)

        array   = less + [array[0]] + greater
        collector.append(' '.join(str(val) for val in array))

        return array


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    n     = lines[0][0]
    ar    = lines[1]

    col   = []
    ar    = partition(ar, col)

    print(' '.join(str(val) for val in ar))
    print()
    print('\n'.join(str(val) for val in col))


if __name__ == "__main__":
    main(sys.argv[1:])

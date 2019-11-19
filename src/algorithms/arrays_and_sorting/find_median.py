import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

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


    def median(array):
        k = len(array) // 2

        while True:
            p = partition(array, 0, len(array) - 1)

            if k < p:
                array = array[:p]
            elif k > p:
                array  = array[p + 1:]
                k -= p + 1
            else:
                return array[p]


    def main():
        n  = int(input())
        ar = [int(i) for i in input().split()]

        print(median(ar))


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


def median(array):
    k = len(array) // 2

    while True:
        p = partition(array, 0, len(array) - 1)

        if k < p:
            array = array[:p]
        elif k > p:
            array  = array[p + 1:]
            k -= p + 1
        else:
            return array[p]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    n     = lines[0][0]
    ar    = lines[1]

    print(median(ar))


if __name__ == "__main__":
    main(sys.argv[1:])

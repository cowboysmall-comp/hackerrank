import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    original implementation:

    def binary_search(array, key, start, end):
        if end < start:
            return -1
        else:
            midpoint = start + (end - start) // 2

            if key < array[midpoint]:
                return binary_search(array, key, start, midpoint - 1)
            elif key > array[midpoint]:
                return binary_search(array, key, midpoint + 1, end)
            else:
                return midpoint


    alternative implementation:

    def binary_search(array, key, start, end):
        while start <= end:
            midpoint = start + (end - start) // 2

            if key < array[midpoint]:
                end   = midpoint - 1
            elif key > array[midpoint]:
                start = midpoint + 1
            else:
                return midpoint

        return -1


    submitted code:

    def binary_search(array, key, start, end):
        while start < end:
            midpoint = start + (end - start) // 2
            if array[midpoint] < key:
                start = midpoint + 1
            else:
                end   = midpoint

        if start == end and array[start] == key:
            return start
        else:
            return -1


    def main():
        V  = int(input())
        n  = int(input())
        ar = [int(i) for i in input().split()]

        print(binary_search(ar, V, 0, n - 1))


    if __name__ == "__main__":
        main()

'''

def binary_search(array, key, start, end):
    while start < end:
        midpoint = start + (end - start) // 2

        if array[midpoint] < key:
            start = midpoint + 1
        else:
            end   = midpoint

    if start == end and array[start] == key:
        return start
    else:
        return -1


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    V     = lines[0][0]
    n     = lines[1][0]
    ar    = lines[2]

    print(binary_search(ar, V, 0, n - 1))


if __name__ == "__main__":
    main(sys.argv[1:])

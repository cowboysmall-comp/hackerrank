import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def count_elements(array):
        counter = [0 for _ in range(100)]

        for val in array:
            counter[val] += 1

        return counter


    def counting_sort(array):
        counts = count_elements(array)
        arrray = []

        for index, count in enumerate(counts):
            arrray.extend([index for _ in range(count)])

        return arrray


    def main():
        n  = int(input())
        ar = [int(i) for i in input().split()]

        print(' '.join(str(val) for val in counting_sort(ar)))


    if __name__ == "__main__":
        main()

'''


def count_elements(array):
    counter = [0 for _ in range(100)]

    for val in array:
        counter[val] += 1

    return counter


def counting_sort(array):
    counts = count_elements(array)
    arrray = []

    for index, count in enumerate(counts):
        arrray.extend([index for _ in range(count)])

    return arrray


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    n     = lines[0][0]
    ar    = lines[1]

    print(' '.join(str(val) for val in counting_sort(ar)))


if __name__ == "__main__":
    main(sys.argv[1:])

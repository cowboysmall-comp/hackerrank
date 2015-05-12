import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from enum import Enum


'''
    submitted code:

    def almost_sorted(array):
        increasing = []
        decreasing = []

        def fits(start, end):
            return array[end - 1] <= array[start] <= array[end + 1]

        for i in range(1, len(array) - 1):
            if array[i - 1] < array[i] > array[i + 1]:
                increasing.append(i)
            if array[i - 1] > array[i] < array[i + 1]:
                decreasing.append(i)

        if len(increasing) == 0 and len(decreasing) == 0:
            return Sorted.yes, None

        if len(increasing) == 1 and len(decreasing) == 1:
            if fits(increasing[0], decreasing[0]) and fits(decreasing[0], increasing[0]):
                return Sorted.swap if decreasing[0] - increasing[0] <= 2 else Sorted.reverse, (increasing[0], decreasing[0])

        if len(increasing) == 2 and len(decreasing) == 2:
            if fits(increasing[0], decreasing[1]) and fits(decreasing[1], increasing[0]):
                return Sorted.swap, (increasing[0], decreasing[1])

        return Sorted.no, None


    def main():
        n     = int(input())
        d     = [-1] + [int(i) for i in input().split()] + [1000001]
        s, p  = almost_sorted(d)

        if s is not Sorted.no:
            print('yes')
            if p:
                print('%s %s %s' % (s.name, p[0], p[1]))
        else:
            print('no')


    if __name__ == "__main__":
        main()

'''

Sorted = Enum('Sorted', 'yes reverse swap no')


def almost_sorted(array):
    increasing = []
    decreasing = []

    def fits(start, end):
        return array[end - 1] <= array[start] <= array[end + 1]

    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] > array[i + 1]:
            increasing.append(i)
        if array[i - 1] > array[i] < array[i + 1]:
            decreasing.append(i)

    if len(increasing) == 0 and len(decreasing) == 0:
        return Sorted.yes, None

    if len(increasing) == 1 and len(decreasing) == 1:
        if fits(increasing[0], decreasing[0]) and fits(decreasing[0], increasing[0]):
            return Sorted.swap if decreasing[0] - increasing[0] <= 2 else Sorted.reverse, (increasing[0], decreasing[0])

    if len(increasing) == 2 and len(decreasing) == 2:
        if fits(increasing[0], decreasing[1]) and fits(decreasing[1], increasing[0]):
            return Sorted.swap, (increasing[0], decreasing[1])

    return Sorted.no, None


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    n     = lines[0][0]
    d     = [-1] + lines[1] + [1000001]
    s, p  = almost_sorted(d)

    if s is not Sorted.no:
        print('yes')
        if p:
            print('%s %s %s' % (s.name, p[0], p[1]))
    else:
        print('no')


if __name__ == "__main__":
    main(sys.argv[1:])

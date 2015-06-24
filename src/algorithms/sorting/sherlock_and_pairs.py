import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def count_elements(A):
        counter = [0 for _ in range(1000001)]

        for val in A:
            counter[val] += 1

        return counter


    def count_pairs(A):
        counter = count_elements(A)
        count   = 0

        for val in counter:
            if val > 1:
                count += val * (val - 1)

        return count


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            A = [int(i) for i in input().split()]
            print(count_pairs(A))


    if __name__ == "__main__":
        main()

'''


def count_elements(A):
    counter = [0 for _ in range(1000001)]

    for val in A:
        counter[val] += 1

    return counter


def count_pairs(A):
    counter = count_elements(A)
    count   = 0

    for val in counter:
        if val > 1:
            count += val * (val - 1)

    return count


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N = lines[(2 * i) + 1][0]
        A = lines[(2 * i) + 2]
        print(count_pairs(A))


if __name__ == "__main__":
    main(sys.argv[1:])

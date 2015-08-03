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


    def count_leq(array):
        counts = count_elements(array)
        L      = [counts[0]]

        for i in range(1, len(counts)):
            L.append(counts[i] + L[i - 1])

        return L


    def main():
        n  = int(input())
        ar = [int(input().split()[0]) for _ in range(n)]

        print(' '.join(str(val) for val in count_leq(ar)))


    if __name__ == "__main__":
        main()

'''

def count_elements(array):
    counter = [0 for _ in range(100)]

    for val in array:
        counter[val] += 1

    return counter


def count_leq(array):
    counts = count_elements(array)
    L      = [counts[0]]

    for i in range(1, len(counts)):
        L.append(counts[i] + L[i - 1])

    return L


def main(argv):
    lines  = files.read_lines_of_words(argv[0])
    n      = int(lines[0][0])
    ar     = [int(line[0]) for line in lines[1:]]

    print(' '.join(str(val) for val in count_leq(ar)))


if __name__ == "__main__":
    main(sys.argv[1:])

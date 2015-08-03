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


    def sort_values(count, array):
        M = count // 2
        L = count_leq([val[0] for val in array])
        S = [None for _ in range(count)]

        for index, value in enumerate(reversed(array)):
            S[L[value[0]] - 1] = value[1] if index < M else '-'
            L[value[0]] -= 1

        return S


    def main():
        n  = int(input())
        ar = []

        for _ in range(n):
            val = input().split()
            ar.append((int(val[0]), val[1]))

        print(' '.join(sort_values(n, ar)))


    if __name__ == "__main__":
        main()


    alternative implementation:

    def sort_values(count, array):
        M = count // 2
        C = [0] + count_leq([val[0] for val in array])[:-1]
        S = [None for _ in range(count)]

        for index, value in enumerate(array):
            S[C[value[0]]] = value[1] if index >= M else '-'
            C[value[0]] += 1

        return S

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


def sort_values(count, array):
    M = count // 2
    L = count_leq([val[0] for val in array])
    S = [None for _ in range(count)]

    for index, value in enumerate(reversed(array)):
        S[L[value[0]] - 1] = value[1] if index < M else '-'
        L[value[0]] -= 1

    return S


def main(argv):
    lines = files.read_lines_of_words(argv[0])
    n     = int(lines[0][0])
    ar    = [(int(line[0]), line[1]) for line in lines[1:]]

    print(' '.join(sort_values(n, ar)))


if __name__ == "__main__":
    main(sys.argv[1:])

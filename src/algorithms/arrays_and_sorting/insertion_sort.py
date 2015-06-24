import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def merge(A, B):
        lengthA    = len(A)
        lengthB    = len(B)
        merged     = []
        inversions = 0

        i = 0
        j = 0

        while i < lengthA and j < lengthB:
            if A[i] > B[j]:
                merged.append(B[j])
                inversions += lengthA - i
                j += 1
            else:
                merged.append(A[i])
                i += 1

        return merged + A[i:] + B[j:], inversions


    def merge_sort(A):
        length = len(A)

        if length > 1:
            A1, I1 = merge_sort(A[:length // 2])
            A2, I2 = merge_sort(A[length // 2:])
            AM, IM = merge(A1, A2)
            return AM, I1 + I2 + IM
        else:
            return A, 0


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            a = [int(i) for i in input().split()]
            print(merge_sort(a)[1])


    if __name__ == "__main__":
        main()


    alternative, brute-force, approach:

    def count_inversions(A):
        l = len(A)
        c = 0

        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    c += 1

        return c


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            a = [int(i) for i in input().split()]
            print(count_inversions(a))


    if __name__ == "__main__":
        main()

'''


def merge(A, B):
    lengthA    = len(A)
    lengthB    = len(B)
    merged     = []
    inversions = 0

    i = 0
    j = 0

    while i < lengthA and j < lengthB:
        if A[i] > B[j]:
            merged.append(B[j])
            inversions += lengthA - i
            j += 1
        else:
            merged.append(A[i])
            i += 1

    return merged + A[i:] + B[j:], inversions


def merge_sort(A):
    length = len(A)

    if length > 1:
        A1, I1 = merge_sort(A[:length // 2])
        A2, I2 = merge_sort(A[length // 2:])
        AM, IM = merge(A1, A2)
        return AM, I1 + I2 + IM
    else:
        return A, 0


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N = lines[(2 * i) + 1][0]
        a = lines[(2 * i) + 2]
        print(merge_sort(a)[1])


if __name__ == "__main__":
    main(sys.argv[1:])

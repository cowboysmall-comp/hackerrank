import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def max_index_product(N, A):
        L = [0 for _ in range(N)]
        R = [0 for _ in range(N)]

        for i in range(1, N):
            pos = i - 1

            while pos >= 0:
                if A[pos] > A[i]:
                    L[i] = pos + 1
                    break
                pos = L[pos] - 1


        for i in range(N - 2, -1, -1):
            pos = i + 1

            while pos >= 0:
                if A[pos] > A[i]:
                    R[i] = pos + 1
                    break
                pos = R[pos] - 1

        return max(x * y for x, y in zip(L, R))


    def main():
        N = int(input())
        A = [int(i) for i in input().split()]

        print(max_index_product(N, A))


    if __name__ == "__main__":
        main()

'''

def max_index_product(N, A):
    L     = [0 for _ in range(N)]
    R     = [0 for _ in range(N)]

    for i in range(1, N):
        pos = i - 1

        while pos >= 0:
            if A[pos] > A[i]:
                L[i] = pos + 1
                break
            pos = L[pos] - 1


    for i in range(N - 2, -1, -1):
        pos = i + 1

        while pos >= 0:
            if A[pos] > A[i]:
                R[i] = pos + 1
                break
            pos = R[pos] - 1

    return max(x * y for x, y in zip(L, R))


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    A     = lines[1]

    print(max_index_product(N, A))


if __name__ == "__main__":
    main(sys.argv[1:])

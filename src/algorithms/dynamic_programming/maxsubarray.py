import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def maximum_contiguous_subarray(A):
        C = A[0]
        M = A[0]

        for a in A[1:]:
            C = max(a, C + a)
            M = max(M, C)

        return M


    def maximum_non_contiguous_subarray(A):
        S = [a for a in A if a > 0]
        if S:
            return sum(S)
        else:
            return max(A)


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            A = [int(i) for i in input().split()]
            print(maximum_contiguous_subarray(A), maximum_non_contiguous_subarray(A))


    if __name__ == "__main__":
        main()

'''

def maximum_contiguous_subarray(A):
    C = A[0]
    M = A[0]

    for a in A[1:]:
        C = max(a, C + a)
        M = max(M, C)

    return M


def maximum_non_contiguous_subarray(A):
    S = [a for a in A if a > 0]
    if S:
        return sum(S)
    else:
        return max(A)


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N = lines[(2 * i) + 1][0]
        A = lines[(2 * i) + 2]
        print(maximum_contiguous_subarray(A), maximum_non_contiguous_subarray(A))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code: Python code too slow...

    def maximum_length(P, Q, S):
        m = len(P)

        T = [[0 for _ in range(m)] for _ in range(m)]

        for i in range(m):
            for j in range(m):
                T[i][j] = P[i] != Q[j]

        M = -1

        for i in range(m):

            if m - i <= M:
                break

            fs1,  fs2  =  0,  0
            bs1,  bs2  =  0,  0
            ptr1, ptr2 = -1, -1

            for j in range(m - i):

                fs1 += T[j][i + j]
                fs2 += T[i + j][j]

                while fs1 - bs1 > S:
                    ptr1 += 1
                    bs1  += T[ptr1][i + ptr1]

                while fs2 - bs2 > S:
                    ptr2 += 1
                    bs2  += T[i + ptr2][ptr2]

                M = max(j - ptr1, j - ptr2, M)

        return M


    def main():
        T = int(input())

        for _ in range(T):
            S, P, Q = [v for v in input().split()]
            print(maximum_length(P, Q, int(S)))


    if __name__ == "__main__":
        main()

'''

def calculate_length(P, Q, S):
    m = min(len(P), len(Q))

    R = [-1]
    M = 0
    c = 0

    for i in range(m):
        if P[i] != Q[i]:
            R.append(i)
            c += 1

            if c > S:
                L = R[-1] - R[-2 - S] - 1
                if L > M:
                    M = L

    if c <= S:
        return m

    return M


def maximum_length(P, Q, S):
    m = len(P)
    M = 0

    L = calculate_length(P, Q, S)
    if M < L:
        M = L

    for i in range(1, m):
        if m - i <= M:
            break

        L = calculate_length(P[i:], Q, S)
        if M < L:
            M = L

        L = calculate_length(P, Q[i:], S)
        if M < L:
            M = L

    return M


def main(argv):
    lines = files.read_lines_of_words(argv[0])
    T     = int(lines[0][0])

    for S, P, Q in lines[1:]:
        print(maximum_length(P, Q, int(S)))


if __name__ == "__main__":
    main(sys.argv[1:])

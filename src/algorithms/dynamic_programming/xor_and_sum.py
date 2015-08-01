import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def xor_and_sum(a, b):
        C = [[0 for _ in range(2)] for _ in range(1000000)]
        A = [0 for _ in range(1000000)]
        B = [0 for _ in range(1000000)]
        P = [0 for _ in range(1000000)]


        L = len(a)
        M = len(b)
        for i in range(L):
            A[L - i - 1] = int(a[i])
        for i in range(M):
            B[M - i - 1] = int(b[i])


        C[0][0] = (B[0] == 0)
        C[0][1] = (B[0] == 1)
        for i in range(1, M + 314159):
            C[i][0] = C[i - 1][0] + (B[i] == 0)
            C[i][1] = C[i - 1][1] + (B[i] == 1)


        P[0] = 1
        for i in range(1, M + 314159):
            P[i]  = P[i - 1] * 2
            P[i] %= 1000000007


        T = P[0] * ((A[0] * (C[0][0] + 314159)) + ((A[0] ^ 1) * C[0][1]))
        for i in range(1, M + 314159):
            if i < 314159:
                T1 = C[i][0] - i + 314159
                T2 = C[i][1]
            else:
                T1 = C[M - 1][0] - C[i - 314159 - 1][0] + 314159
                T2 = C[M - 1][1] - C[i - 314159 - 1][1]

            T += P[i] * ((A[i] * T1) + ((A[i] ^ 1) * T2))
            T %= 1000000007


        return T


    def main():
        a = input()
        b = input()

        print(xor_and_sum(a, b))


    if __name__ == "__main__":
        main()

'''

def xor_and_sum(a, b):
    C = [[0 for _ in range(2)] for _ in range(1000000)]
    A = [0 for _ in range(1000000)]
    B = [0 for _ in range(1000000)]
    P = [0 for _ in range(1000000)]


    L = len(a)
    M = len(b)
    for i in range(L):
        A[L - i - 1] = int(a[i])
    for i in range(M):
        B[M - i - 1] = int(b[i])


    C[0][0] = (B[0] == 0)
    C[0][1] = (B[0] == 1)
    for i in range(1, M + 314159):
        C[i][0] = C[i - 1][0] + (B[i] == 0)
        C[i][1] = C[i - 1][1] + (B[i] == 1)


    P[0] = 1
    for i in range(1, M + 314159):
        P[i]  = P[i - 1] * 2
        P[i] %= 1000000007


    T = P[0] * ((A[0] * (C[0][0] + 314159)) + ((A[0] ^ 1) * C[0][1]))
    for i in range(1, M + 314159):
        if i < 314159:
            T1 = C[i][0] - i + 314159
            T2 = C[i][1]
        else:
            T1 = C[M - 1][0] - C[i - 314159 - 1][0] + 314159
            T2 = C[M - 1][1] - C[i - 314159 - 1][1]

        T += P[i] * ((A[i] * T1) + ((A[i] ^ 1) * T2))
        T %= 1000000007


    return T


def main(argv):
    lines = files.read_lines(argv[0])
    a     = lines[0]
    b     = lines[1]

    print(xor_and_sum(a, b))


if __name__ == "__main__":
    main(sys.argv[1:])

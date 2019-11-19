import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def hexagonal_grid(N, A, B):
        T = 2 * N
        C = [0 for _ in range(T)]
        D = []


        for i in range(len(A)):
            D.append(int(A[i]))
            D.append(int(B[i]))


        L = (T - 1 - D[::-1].index(0)) if 0 in D else 0


        if D[0] != 0:
            C[0] = 1
        else:
            if N > 0:
                C[1] = 1 - D[1]
            if N > 1:
                C[2] = D[1] - D[2]


        for i in range(1, T):
            if D[i] != 0:
                C[i] = C[i - 1]
            elif C[i - 1] != 0:
                if i < T - 1:
                    C[i + 1] = 1 - D[i + 1]
                if i < T - 2:
                    C[i + 2] = D[i + 1] - D[i + 2]


        return 'YES' if C[L] != 0 else 'NO'


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            A = input()
            B = input()
            print(hexagonal_grid(N, A, B))


    if __name__ == "__main__":
        main()

'''

def hexagonal_grid(N, A, B):
    T = 2 * N
    C = [0 for _ in range(T)]
    D = []


    for i in range(len(A)):
        D.append(int(A[i]))
        D.append(int(B[i]))


    L = (T - 1 - D[::-1].index(0)) if 0 in D else 0


    if D[0] != 0:
        C[0] = 1
    else:
        if N > 0:
            C[1] = 1 - D[1]
        if N > 1:
            C[2] = D[1] - D[2]


    for i in range(1, T):
        if D[i] != 0:
            C[i] = C[i - 1]
        elif C[i - 1] != 0:
            if i < T - 1:
                C[i + 1] = 1 - D[i + 1]
            if i < T - 2:
                C[i + 2] = D[i + 1] - D[i + 2]


    return 'YES' if C[L] != 0 else 'NO'


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    for i in range(T):
        N = int(lines[(3 * i) + 1])
        A = lines[(3 * i) + 2]
        B = lines[(3 * i) + 3]
        print(hexagonal_grid(N, A, B))


if __name__ == "__main__":
    main(sys.argv[1:])

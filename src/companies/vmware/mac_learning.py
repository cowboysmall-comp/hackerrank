import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def is_multicast(A):
        return int(A[0:2], 16) & 1 == 1


    def add_mapping(M, C, K, V):
        if len(M) == 16 and C[0] in M:
            M.pop(C.pop(0), None)
        M[K] = V
        C.append(K)


    def mac_learning(M, C, P):
        if is_multicast(P[2]):
            return 'drop'

        if P[2] not in M or M[P[2]] != P[0]:
            add_mapping(M, C, P[2], P[0])

        if is_multicast(P[1]) or P[1] not in M:
            return 'flood'

        if P[0] == M[P[1]]:
            return 'drop'

        return M[P[1]]


    def main():
        N = int(input())
        M = {}
        C = []

        for _ in range(N):
            P = [i for i in input().split()]
            print(mac_learning(M, C, (int(P[0]), P[1], P[2])))


    if __name__ == "__main__":
        main()

'''

def is_multicast(A):
    return int(A[0:2], 16) & 1 == 1


def add_mapping(M, C, K, V):
    if len(M) == 16 and C[0] in M:
        M.pop(C.pop(0), None)
    M[K] = V
    C.append(K)


def mac_learning(M, C, P):
    if is_multicast(P[2]):
        return 'drop'

    if P[2] not in M or M[P[2]] != P[0]:
        add_mapping(M, C, P[2], P[0])

    if is_multicast(P[1]) or P[1] not in M:
        return 'flood'

    if P[0] == M[P[1]]:
        return 'drop'

    return M[P[1]]


def main(argv):
    lines = files.read_lines_of_words(argv[0])

    N     = int(lines[0][0])
    M     = {}
    C     = []

    for p in lines[1:]:
        P = int(p[0]), p[1], p[2]
        print(mac_learning(M, C, P))


if __name__ == "__main__":
    main(sys.argv[1:])

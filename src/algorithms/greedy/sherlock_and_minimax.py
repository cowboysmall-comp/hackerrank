import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

import heapq


'''
    submitted code:

    def minimax(N, A, P, Q):
        def minimum(x):
            return min(abs(x - a) for a in A)

        V = P
        M = minimum(P)

        for i in range(N):
            for j in range(i + 1, N):
                v = (A[i] + A[j]) // 2
                if P <= v <= Q:
                    m = minimum(v)
                    if m > M:
                        V = v
                        M = m

        return Q if minimum(Q) > M else V


    def main():
        N    = int(input())
        A    = sorted([int(i) for i in input().split()])
        P, Q = [int(i) for i in input().split()]

        print(minimax(N, A, P, Q))


    if __name__ == "__main__":
        main()

'''

def minimax(N, A, P, Q):
    def minimum(x):
        return min(abs(x - a) for a in A)

    V = P
    M = minimum(P)

    for i in range(N):
        for j in range(i + 1, N):
            v = (A[i] + A[j]) // 2
            if P <= v <= Q:
                m = minimum(v)
                if m > M:
                    V = v
                    M = m

    return Q if minimum(Q) > M else V


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    A     = sorted(lines[1])
    P, Q  = lines[2]

    print(minimax(N, A, P, Q))


if __name__ == "__main__":
    main(sys.argv[1:])





# def minimax(N, A, P, Q):
#     V = 0
#     I = N + 1

#     for i in range(P, Q + 1):
#         m = []
#         for a in A:
#             heapq.heappush(m, abs(a - i))

#         v = heapq.heappop(m)
#         print(v)
#         if v > V or v == V and i < I:
#             V, I = v, i

#     return I

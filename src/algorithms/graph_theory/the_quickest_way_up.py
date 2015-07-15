import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict

import heapq


'''
    submitted code:

    def dijkstra(S, N, G):
        D    = {}
        H    = [(0, S)]

        for n in range(1, N + 1):
            D[n] = 999999

        D[S] = 0

        while H:
            t = heapq.heappop(H)
            for h in G[t[1]]:
                if D[h[1]] > D[t[1]] + h[0]:
                    D[h[1]] = D[t[1]] + h[0]
                    if h in H:
                        H.remove(h)
                        heapq.heapify(H)
                    heapq.heappush(H, (D[h[1]], h[1]))

        return D[100]


    def main():
        T = int(input())

        for _ in range(T):
            N  = int(input())

            S  = {}
            for _ in range(N):
                e = [int(i) for i in input().split()]
                S[e[0]] = e[1]

            M  = int(input())

            L  = {}
            for _ in range(M):
                e = [int(i) for i in input().split()]
                L[e[0]] = e[1]

            G  = defaultdict(set)
            for i in range(1, 101):
                for j in range(i + 1, i + 7):
                    if j <= 100:
                        if j in S:
                            G[i].add((1, S[j]))
                        elif j in L:
                            G[i].add((1, L[j]))
                        else:
                            G[i].add((1, j))

            D  = dijkstra(1, 100, G)
            print(D if D != 999999 else '-1')


    if __name__ == "__main__":
        main()

'''


def dijkstra(S, N, G):
    D    = {}
    H    = [(0, S)]

    for n in range(1, N + 1):
        D[n] = 999999

    D[S] = 0

    while H:
        t = heapq.heappop(H)
        for h in G[t[1]]:
            if D[h[1]] > D[t[1]] + h[0]:
                D[h[1]] = D[t[1]] + h[0]
                if h in H:
                    H.remove(h)
                    heapq.heapify(H)
                heapq.heappush(H, (D[h[1]], h[1]))

    return D[100]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    T     = lines[0][0]
    C     = 1

    for _ in range(T):
        N  = lines[C][0]
        C += 1

        S  = {}
        for line in lines[C:C + N]:
            S[line[0]] = line[1]
        C += N

        M  = lines[C][0]
        C += 1

        L  = {}
        for line in lines[C:C + M]:
            L[line[0]] = line[1]
        C += M

        G  = defaultdict(set)
        for i in range(1, 101):
            for j in range(i + 1, i + 7):
                if j <= 100:
                    if j in S:
                        G[i].add((1, S[j]))
                    elif j in L:
                        G[i].add((1, L[j]))
                    else:
                        G[i].add((1, j))

        D  = dijkstra(1, 100, G)
        print(D if D != 999999 else '-1')


if __name__ == "__main__":
    main(sys.argv[1:])

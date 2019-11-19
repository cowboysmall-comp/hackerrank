import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

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

        return D


    def main():
        T = int(input())

        for _ in range(T):
            N, M = [int(i) for i in input().split()]

            G    = defaultdict(set)

            for _ in range(M):
                e = [int(i) for i in input().split()]
                G[e[0]].add((e[2], e[1]))
                G[e[1]].add((e[2], e[0]))

            S    = int(input())

            D    = dijkstra(S, N, G)
            print(' '.join(str(D[n]) if D[n] != 999999 else '-1' for n in range(1, N + 1) if n != S))


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

    return D


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    T     = lines[0][0]
    C     = 1

    for _ in range(T):
        N, M = lines[C]
        C   += 1

        G    = defaultdict(set)
        for line in lines[C:C + M]:
            G[line[0]].add((line[2], line[1]))
            G[line[1]].add((line[2], line[0]))
        C   += M

        S    = lines[C][0]
        C   += 1

        D    = dijkstra(S, N, G)
        print(' '.join(str(D[n]) if D[n] != 999999 else '-1' for n in range(1, N + 1) if n != S))


if __name__ == "__main__":
    main(sys.argv[1:])

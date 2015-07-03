import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict, deque


'''
    submitted code:

    def breadth_first_search(S, N, G, L = 1):
        C = {}

        for n in range(1, N + 1):
            C[n] = -1

        C[S]  = 0
        Q     = deque([S])

        while Q:
            n = Q.popleft()
            for h in G[n]:
                if C[h] == -1:
                    C[h]  = C[n] + L
                    Q.append(h)

        return C


    def main():
        T = int(input())

        for _ in range(T):
            N, M = [int(i) for i in input().split()]

            G    = defaultdict(set)

            for _ in range(M):
                E = [int(i) for i in input().split()]
                G[E[0]].add(E[1])
                G[E[1]].add(E[0])

            S    = int(input())

            D    = breadth_first_search(S, N, G, 6)
            print(' '.join(str(D[n]) for n in range(1, N + 1) if n != S))


    if __name__ == "__main__":
        main()

'''


def breadth_first_search(S, N, G, L = 1):
    C    = {}

    for n in range(1, N + 1):
        C[n] = -1

    C[S] = 0
    Q    = deque([S])

    while Q:
        n = Q.popleft()
        for h in G[n]:
            if C[h] == -1:
                C[h] = C[n] + L
                Q.append(h)

    return C


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    T     = lines[0][0]
    C     = 0

    for _ in range(T):
        C   += 1
        N, M = lines[C]

        C   += 1
        G    = defaultdict(set)

        for line in lines[C:C + M]:
            G[line[0]].add(line[1])
            G[line[1]].add(line[0])

        C   += M
        S    = lines[C][0]

        D    = breadth_first_search(S, N, G, 6)
        print(' '.join(str(D[n]) for n in range(1, N + 1) if n != S))


if __name__ == "__main__":
    main(sys.argv[1:])

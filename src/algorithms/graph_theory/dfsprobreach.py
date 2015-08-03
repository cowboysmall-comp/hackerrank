import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def depth_first_search(S, G):
        E = defaultdict(int)
        T = []

        def explore(N):
            E[N] += 1

            for n in G[N]:
                if E[n] == 0:
                    explore(n)

            T.append(N)

        explore(S)

        return T


    def rounding(S):
        return int(int((S * 1000000000) + 0.5) / 1000000000)


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            G = defaultdict(list)

            I  = 1
            for _ in range(N + 1):
                for H in input().split()[1:]:
                    G[int(H)].append(I)
                I += 1

            P  = [float(w) for w in input().split()]

            CC = depth_first_search(N + 1, G)
            print(rounding(sum(P[n - 1] for n in CC[:-1])))


    if __name__ == "__main__":
        main()

'''

def depth_first_search(S, G):
    E = defaultdict(int)
    T = []

    def explore(N):
        E[N] += 1

        for n in G[N]:
            if E[n] == 0:
                explore(n)

        T.append(N)

    explore(S)

    return T


def rounding(S):
    return int(int((S * 1000000000) + 0.5) / 1000000000)


def main(argv):
    lines = files.read_lines_of_words(argv[0])

    T     = int(lines[0][0])
    C     = 0

    for _ in range(T):
        C += 1
        N  = int(lines[C][0])

        C += 1
        G  = defaultdict(list)

        I  = 0
        for line in lines[C:C + N + 1]:
            I += 1
            for H in line[1:]:
                G[int(H)].append(I)

        C += I
        P  = [float(w) for w in lines[C]]

        CC = depth_first_search(N + 1, G)
        print(rounding(sum(P[n - 1] for n in CC[:-1])))


if __name__ == "__main__":
    main(sys.argv[1:])

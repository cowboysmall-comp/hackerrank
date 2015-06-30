import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

import operator


'''
    submitted code:

    class UnionFind:

        def __init__(self, N):
            self.P = [i for i in range(N + 1)]

        def find(self, V):
            while V != self.P[V]:
                V = self.P[V]
            return V

        def connected(self, P, Q):
            return self.find(P) == self.find(Q)

        def union(self, P, Q):
            PP = self.find(P)
            QP = self.find(Q)
            self.P[PP] = QP


    def kruskal(S, N, E):
        uf = UnionFind(N)
        T  = []

        for e in sorted(E, key = operator.itemgetter(0, 1)):
            if not uf.connected(e[2], e[3]):
                uf.union(e[2], e[3])
                T.append((e[2], e[3], e[0]))

        return T


    def main():
        N, M = [int(i) for i in input().split()]

        E    = []

        for _ in range(M):
            e = [int(i) for i in input().split()]
            E.append((e[2], e[0] + e[1] + e[2], e[0], e[1]))
            E.append((e[2], e[0] + e[1] + e[2], e[1], e[0]))

        S    = int(input())

        print(sum(t[2] for t in kruskal(S, N, E)))


    if __name__ == "__main__":
        main()

'''


class UnionFind:

    def __init__(self, N):
        self.P = [i for i in range(N + 1)]

    def find(self, V):
        while V != self.P[V]:
            V = self.P[V]
        return V

    def connected(self, P, Q):
        return self.find(P) == self.find(Q)

    def union(self, P, Q):
        PP = self.find(P)
        QP = self.find(Q)
        self.P[PP] = QP


def kruskal(S, N, E):
    uf = UnionFind(N)
    T  = []

    for e in sorted(E, key = operator.itemgetter(0, 1)):
        if not uf.connected(e[2], e[3]):
            uf.union(e[2], e[3])
            T.append((e[2], e[3], e[0]))

    return T


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, M  = lines[0]

    E     = []

    for line in lines[1:M + 1]:
        E.append((line[2], line[0] + line[1] + line[2], line[0], line[1]))
        E.append((line[2], line[0] + line[1] + line[2], line[1], line[0]))

    S     = lines[M + 1][0]

    print(sum(t[2] for t in kruskal(S, N, E)))


if __name__ == "__main__":
    main(sys.argv[1:])

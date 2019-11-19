import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    class UnionFind:

        def __init__(self, N):
            self.N = N
            self.P = [i for i in range(N)]
            self.S = [1 for _ in range(N)]

        def find(self, V):
            while V != self.P[V]:
                V = self.P[V]
            return V

        def connected(self, P, Q):
            return self.find(P) == self.find(Q)

        def union(self, P, Q):
            PP = self.find(P)
            QP = self.find(Q)
            if PP != QP:
                if self.S[PP] < self.S[QP]:
                    self.P[PP]  = QP
                    self.S[QP] += self.S[PP]
                else:
                    self.P[QP]  = PP
                    self.S[PP] += self.S[QP]

        def get_sizes(self):
            return [self.S[i] for i in range(self.N) if i == self.P[i]]


    def journey_to_the_moon(N, P):
        uf = UnionFind(N)

        for p in P:
            uf.union(p[0], p[1])

        T = N * (N - 1) // 2
        for S in uf.get_sizes():
            if S > 1:
                T -= S * (S - 1) // 2

        return T


    def main():
        N, I = [int(i) for i in input().split()]

        P    = []
        for _ in range(I):
            P.append([int(i) for i in input().split()])

        print(journey_to_the_moon(N, P))


    if __name__ == "__main__":
        main()

'''

class UnionFind:

    def __init__(self, N):
        self.N = N
        self.P = [i for i in range(N)]
        self.S = [1 for _ in range(N)]

    def find(self, V):
        while V != self.P[V]:
            V = self.P[V]
        return V

    def connected(self, P, Q):
        return self.find(P) == self.find(Q)

    def union(self, P, Q):
        PP = self.find(P)
        QP = self.find(Q)
        if PP != QP:
            if self.S[PP] < self.S[QP]:
                self.P[PP]  = QP
                self.S[QP] += self.S[PP]
            else:
                self.P[QP]  = PP
                self.S[PP] += self.S[QP]

    def get_sizes(self):
        return [self.S[i] for i in range(self.N) if i == self.P[i]]


def journey_to_the_moon(N, P):
    uf = UnionFind(N)

    for p in P:
        uf.union(p[0], p[1])

    T = N * (N - 1) // 2
    for S in uf.get_sizes():
        if S > 1:
            T -= S * (S - 1) // 2

    return T


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    N, I = lines[0]
    P    = lines[1:]

    print(journey_to_the_moon(N, P))


if __name__ == "__main__":
    main(sys.argv[1:])

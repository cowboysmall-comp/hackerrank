import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    class BIT:

        def __init__(self):
            self.N = 50010
            self.T = [0 for _ in range(50010)]

        def get(self, i):
            return query(i) - query(i - 1)

        def set(self, i, v):
            update(i, v - self.get(i))

        def update(self, i, v):
            while i <= self.N:
                self.T[i] += v
                self.T[i] %= 1000000007
                i += (i & -i)

        def read(self, i):
            S = 0
            while i > 0:
                S += self.T[i]
                S %= 1000000007
                i -= (i & -i)
            return S


    def candles_counting(N, K, A):
        L = 2 ** K
        T = [BIT() for _ in range(L)]

        T[0].update(1, 1)

        for h, c in A:
            for j in range(L):
                T[j | (2 ** (c - 1))].update(h + 1, T[j].read(h))

        return T[L - 1].read(50001)


    def main():
        N, K = [int(i) for i in input().split()]
        A    = []
        for _ in range(N):
            A.append([int(i) for i in input().split()])

        print(candles_counting(N, K, A))


    if __name__ == "__main__":
        main()

'''

class BIT:

    def __init__(self):
        self.N = 50010
        self.T = [0 for _ in range(50010)]

    def get(self, i):
        return self.query(i) - self.query(i - 1)

    def set(self, i, v):
        self.update(i, v - self.get(i))

    def update(self, i, v):
        while i <= self.N:
            self.T[i] += v
            self.T[i] %= 1000000007
            i += (i & -i)

    def read(self, i):
        S = 0
        while i > 0:
            S += self.T[i]
            S %= 1000000007
            i -= (i & -i)
        return S


def candles_counting(N, K, A):
    L = 2 ** K
    T = [BIT() for _ in range(L)]

    T[0].update(1, 1)

    for i in range(N):
        h, c = A[i]
        for j in range(L):
            T[j | (2 ** (c - 1))].update(h + 1, T[j].read(h))

    return T[L - 1].read(50001)


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, K  = lines[0]
    A     = lines[1:]

    print(candles_counting(N, K, A))


if __name__ == "__main__":
    main(sys.argv[1:])

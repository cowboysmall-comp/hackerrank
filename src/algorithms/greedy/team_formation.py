import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

import heapq


'''
    submitted code:

    def team_formation(N, A):
        D = {}

        def insert(K, V):
            if K in D:
                D[K].append(V)
                heapq.heapify(D[K])
            else:
                D[K] = [V]

        for a in sorted(A):
            if a - 1 in D:
                W = heapq.heappop(D[a - 1])

                insert(a, W + 1)

                if not D[a - 1]:
                    del D[a - 1]
            else:
                insert(a, 1)

        return min(heapq.heappop(D[d]) for d in D)


    def main():
        T = int(input())

        for _ in range(T):
            I    = [int(i) for i in input().split()]
            N, A = I[0], I[1:]

            print(0 if N == 0 else team_formation(N, A))


    if __name__ == "__main__":
        main()

'''

def team_formation(N, A):
    D = {}

    def insert(K, V):
        if K in D:
            D[K].append(V)
            heapq.heapify(D[K])
        else:
            D[K] = [V]

    for a in sorted(A):
        if a - 1 in D:
            W = heapq.heappop(D[a - 1])

            insert(a, W + 1)

            if not D[a - 1]:
                del D[a - 1]
        else:
            insert(a, 1)

    return min(heapq.heappop(D[d]) for d in D)


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for line in lines[1:]:
        N, A  = line[0], line[1:]

        print(0 if N == 0 else team_formation(N, A))


if __name__ == "__main__":
    main(sys.argv[1:])

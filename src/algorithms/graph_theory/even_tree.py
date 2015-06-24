import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def even_tree(G, N):
        X = set()
        S = [1 for _ in range(N + 1)]
        C = [0]

        def dfs(n):
            X.add(n)

            for c in G[n] - X:
                count = dfs(c)
                if count % 2 == 0:
                    C[0] += 1
                else:
                    S[n] += count

            return S[n]

        dfs(1)

        return C[0]


    def main():
        N, M = [int(i) for i in input().split()]

        G    = defaultdict(set)
        for _ in range(M):
            e1, e2 = [int(i) for i in input().split()]
            G[e1].add(e2)
            G[e2].add(e1)

        print(even_tree(G, N))


    if __name__ == "__main__":
        main()

'''

def even_tree(G, N):
    X = set()
    S = [1 for _ in range(N + 1)]
    C = [0]

    def dfs(n):
        X.add(n)

        for c in G[n] - X:
            count = dfs(c)
            if count % 2 == 0:
                C[0] += 1
            else:
                S[n] += count

        return S[n]

    dfs(1)

    return C[0]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    N, M  = lines[0]

    G     = defaultdict(set)
    for e in lines[1:]:
        G[e[0]].add(e[1])
        G[e[1]].add(e[0])

    print(even_tree(G, N))


if __name__ == "__main__":
    main(sys.argv[1:])

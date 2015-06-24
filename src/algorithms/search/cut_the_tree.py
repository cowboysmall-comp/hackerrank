import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def tree_diff(G, V, N):
        S = [node for node in G if len(G[node]) == 1]

        while S:
            l = S.pop()
            for n in G[l]:
                V[n] += V[l]
                G[n].remove(l)
                if len(G[n]) == 1:
                    S.append(n)

        T = V[l]
        M = T

        for i in range(1, N + 1):
            M = min(M, abs(T - (2 * V[i])))

        return M


    def main():
        N = int(input())
        V = [0] + [int(i) for i in input().split()]

        G = defaultdict(set)
        for _ in range(N - 1):
            e1, e2 = [int(i) for i in input().split()]
            G[e1].add(e2)
            G[e2].add(e1)

        print(tree_diff(G, V, N))


    if __name__ == "__main__":
        main()


    alternative implementation - submission of below results in seg fault:

    def tree_diff(G, V, N):
        X = set()

        def dfs(node):
            X.add(node)

            for n in G[node] - X:
                V[node] += dfs(n)

            return V[node]

        root = None
        for n in G:
            if len(G[n]) > 1:
                root = n
                break

        T = dfs(root)
        M = T

        for i in range(1, N + 1):
            M = min(M, abs(T - (2 * V[i])))

        return M


    def main():
        N = int(input())
        V = [0] + [int(i) for i in input().split()]

        G = defaultdict(set)
        for _ in range(N - 1):
            e1, e2 = [int(i) for i in input().split()]
            G[e1].add(e2)
            G[e2].add(e1)

        print(tree_diff(G, V, N))


    if __name__ == "__main__":
        sys.setrecursionlimit(100000)
        main()

'''

def tree_diff(G, V, N):
    S = [node for node in G if len(G[node]) == 1]

    while S:
        l = S.pop()
        for n in G[l]:
            V[n] += V[l]
            G[n].remove(l)
            if len(G[n]) == 1:
                S.append(n)

    T = V[l]
    M = T

    for i in range(1, N + 1):
        M = min(M, abs(T - (2 * V[i])))

    return M


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    N = lines[0][0]
    V = [0] + lines[1]

    G = defaultdict(set)
    for e in lines[2:]:
        G[e[0]].add(e[1])
        G[e[1]].add(e[0])

    print(tree_diff(G, V, N))


if __name__ == "__main__":
    main(sys.argv[1:])

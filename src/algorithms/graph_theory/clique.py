import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def clique(N, M):
        low  = 1
        high = N + 1

        def calculate(N, K):
            g1  = N % K
            g2  = K - g1
            sz2 = N // K
            sz1 = sz2 + 1
            return (g1 * sz1 * g2 * sz2) + (g1 * (g1 - 1) * sz1 * sz1 / 2) + (g2 * (g2 - 1) * sz2 * sz2 / 2)

        while low + 1 < high:
            mid = low + (high - low) // 2
            if calculate(N, mid) < M:
                low  = mid
            else:
                high = mid

        return high


    def main():
        T = int(input())

        for _ in range(T):
            N, M = [int(i) for i in input().split()]
            print(clique(N, M))


    if __name__ == "__main__":
        main()

'''

def clique(N, M):
    low  = 1
    high = N + 1

    def calculate(N, K):
        g1  = N % K
        g2  = K - g1
        sz2 = N // K
        sz1 = sz2 + 1
        return (g1 * sz1 * g2 * sz2) + (g1 * (g1 - 1) * sz1 * sz1 / 2) + (g2 * (g2 - 1) * sz2 * sz2 / 2)

    while low + 1 < high:
        mid = low + (high - low) // 2
        if calculate(N, mid) < M:
            low  = mid
        else:
            high = mid

    return high


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    T     = lines[0][0]

    for N, M in lines[1:]:
        print(clique(N, M))


if __name__ == "__main__":
    main(sys.argv[1:])

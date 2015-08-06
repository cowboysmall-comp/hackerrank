import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def toys(N, W):
        V = [0 for _ in range(10001)]
        C = 0

        for w in W:
            V[w] += 1

        for i in range(10001):
            if V[i]:
                C += 1
                for j in range(5):
                    V[i + j] = 0

        return C


    def main():
        N = int(input())
        W = [int(i) for i in input().split()]

        print(toys(N, W))


    if __name__ == "__main__":
        main()


    alternative implementation:

    def toys(N, W):
        W.sort()

        C = 0
        i = 0

        while i < N:
            C += 1
            j  = i + 1
            while j < N and W[j] <= W[i] + 4:
                j += 1
            i = j

        return C

'''

def toys(N, W):
    V = [0 for _ in range(10001)]
    C = 0

    for w in W:
        V[w] += 1

    for i in range(10001):
        if V[i]:
            C += 1
            for j in range(5):
                V[i + j] = 0

    return C


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    W     = lines[1]

    print(toys(N, W))


if __name__ == "__main__":
    main(sys.argv[1:])

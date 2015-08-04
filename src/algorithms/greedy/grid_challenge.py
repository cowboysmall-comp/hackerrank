import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def grid_challenge(N, G):
        G[0].sort()

        for i in range(1, N):
            G[i].sort()
            for j in range(N):
                if G[i - 1][j] > G[i][j]:
                    return 'NO'

        return 'YES'


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())

            G = []
            for _ in range(N):
                G.append([ord(c) for c in input()])

            print(grid_challenge(N, G))


    if __name__ == "__main__":
        main()

'''

def grid_challenge(N, G):
    G[0].sort()

    for i in range(1, N):
        G[i].sort()
        for j in range(N):
            if G[i - 1][j] > G[i][j]:
                return 'NO'

    return 'YES'


def main(argv):
    lines = files.read_lines(argv[0])

    T     = int(lines[0])
    C     = 1

    for _ in range(T):
        N  = int(lines[C])
        C += 1

        G  = [[ord(c) for c in line] for line in lines[C:C + N]]
        C += N

        print(grid_challenge(N, G))


if __name__ == "__main__":
    main(sys.argv[1:])

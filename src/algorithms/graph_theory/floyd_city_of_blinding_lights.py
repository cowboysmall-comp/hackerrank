import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def floyd(N, G):
        for k in range(N):
            for i in range(N):

                if G[i][k] == 999999:
                    continue

                V = G[i][k]

                for j in range(N):

                    W = G[k][j]

                    if G[i][j] > V + W:
                        G[i][j] = V + W

        return G


    def main():
        N, M = [int(i) for i in raw_input().split()]

        G    = [[999999 for _ in range(N)] for _ in range(N)]

        for n in range(N):
            G[n][n] = 0

        for _ in range(M):
            x, y, r = [int(i) for i in raw_input().split()]
            G[x - 1][y - 1] = r

        D    = floyd(N, G)

        for _ in range(int(raw_input())):
            a, b = [int(i) for i in raw_input().split()]
            d    = D[a - 1][b - 1]
            print('-1' if d == 999999 else d)


    if __name__ == "__main__":
        main()

'''

def floyd(N, G):
    for k in range(N):
        for i in range(N):

            if G[i][k] == 999999:
                continue

            V = G[i][k]

            for j in range(N):

                W = G[k][j]

                if G[i][j] > V + W:
                    G[i][j] = V + W

    return G


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, M  = lines[0]


    G     = [[999999 for _ in range(N)] for _ in range(N)]

    for n in range(N):
        G[n][n] = 0

    for x, y, r in lines[1:M + 1]:
        G[x - 1][y - 1] = r

    D     = floyd(N, G)

    Q     = lines[M + 1][0]
    for a, b in lines[M + 2:]:
        d = D[a - 1][b - 1]
        print('-1' if d == 999999 else d)


if __name__ == "__main__":
    main(sys.argv[1:])

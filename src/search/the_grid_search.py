import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code:

    def grid_search(R, C, G, r, c, P):
        for i in range(R):
            f = G[i].find(P[0])

            if f != -1 and f + c < C:
                count = 1

                for j in range(1, r):
                    if G[i + j][f:f + c] == P[j]:
                        count += 1

                if count == r:
                    return True

        return False


    def main():
        T = int(input())

        for _ in range(T):
            R, C = [int(i) for i in input().split()]
            G    = [input() for _ in range(R)]
            r, c = [int(i) for i in input().split()]
            P    = [input() for _ in range(r)]
            print('YES' if grid_search(R, C, G, r, c, P) else 'NO')


    if __name__ == "__main__":
        main()

'''


def grid_search(R, C, G, r, c, P):
    for i in range(R):
        f = G[i].find(P[0])

        if f != -1 and f + c < C:
            count = 1

            for j in range(1, r):
                if G[i + j][f:f + c] == P[j]:
                    count += 1

            if count == r:
                return True

    return False


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    count = 1
    for _ in range(T):
        R, C   = [int(i) for i in lines[count].split()]
        count += 1
        G      = lines[count:count + R]
        count += R
        r, c   = [int(i) for i in lines[count].split()]
        count += 1
        P      = lines[count:count + r]
        count += r
        print('YES' if grid_search(R, C, G, r, c, P) else 'NO')


if __name__ == "__main__":
    main(sys.argv[1:])

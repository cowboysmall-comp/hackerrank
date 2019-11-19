import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def board_cutting(M, N, Y, X):
        C = sorted(X + Y, reverse = True)

        T, V, H = 0, 0, 0

        for i in range(M + N - 2):
            if C[i][1]:
                T += C[i][0] * (V + 1)
                T %= 1000000007
                H += 1
            else:
                T += C[i][0] * (H + 1)
                T %= 1000000007
                V += 1

        return T


    def main():
        T = int(input())

        for _ in range(T):
            M, N = [int(i) for i in input().split()]
            Y    = [(int(y), 1) for y in input().split()]
            X    = [(int(x), 0) for x in input().split()]

            print(board_cutting(M, N, Y, X))


    if __name__ == "__main__":
        main()

'''

def board_cutting(M, N, Y, X):
    C = sorted(X + Y, reverse = True)

    T, V, H = 0, 0, 0

    for i in range(M + N - 2):
        if C[i][1]:
            T += C[i][0] * (V + 1)
            T %= 1000000007
            H += 1
        else:
            T += C[i][0] * (H + 1)
            T %= 1000000007
            V += 1

    return T


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        M, N = lines[(3 * i) + 1]
        Y    = [(y, 1) for y in lines[(3 * i) + 2]]
        X    = [(x, 0) for x in lines[(3 * i) + 3]]

        print(board_cutting(M, N, Y, X))


if __name__ == "__main__":
    main(sys.argv[1:])

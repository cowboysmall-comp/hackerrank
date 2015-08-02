import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def cost(N, B):
        C = [[0 for _ in range(2)] for _ in range(N)]

        for i in range(1, N):
            C[i][0] = max(C[i - 1][1] + abs(B[i - 1] - 1), C[i - 1][0])
            C[i][1] = max(C[i - 1][0] + abs(B[i] - 1), C[i - 1][1] + abs(B[i] - B[i - 1]))

        return max(C[N - 1])


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            B = [int(i) for i in input().split()]
            print(cost(N, B))


    if __name__ == "__main__":
        main()

'''

def cost(N, B):
    C = [[0 for _ in range(2)] for _ in range(N)]

    for i in range(1, N):
        C[i][0] = max(C[i - 1][1] + abs(B[i - 1] - 1), C[i - 1][0])
        C[i][1] = max(C[i - 1][0] + abs(B[i] - 1), C[i - 1][1] + abs(B[i] - B[i - 1]))

    return max(C[N - 1])



def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N = lines[(2 * i) + 1][0]
        B = lines[(2 * i) + 2]
        print(cost(N, B))


if __name__ == "__main__":
    main(sys.argv[1:])

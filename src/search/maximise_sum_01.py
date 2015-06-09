import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code:

    def maximize_sum(A, M):
        current = 0
        maximum = 0

        for a in A:
            current = max(0, current + a) % M
            maximum = max(maximum, current)

        return maximum


    def main():
        T = int(input())

        for _ in range(T):
            N = int(input())
            A = [int(i) for i in input().split()]
            print('YES' if divisible(N, A) else 'NO')


    if __name__ == "__main__":
        main()

'''




def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N, M = lines[(2 * i) + 1]
        A    = lines[(2 * i) + 2]
        # print(maximize_sum(A, N, M))
        # print(maximize_sum(A, M))
        print(maximize_sum(A, M, 0, N - 1))


if __name__ == "__main__":
    main(sys.argv[1:])

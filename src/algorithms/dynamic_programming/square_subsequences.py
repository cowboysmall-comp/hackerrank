import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def count_square_subsequences(s, t):
        m       = len(s)
        n       = len(t)

        T       = [[0 for _ in range(n)] for _ in range(m)]
        T[0][0] = 1 if s[0] == t[0] else 0

        for i in range(1, m):
            T[i][0]  = T[i - 1][0]
            T[i][0] %= 1000000007

        for j in range(1, n):
            T[0][j]  = T[0][j - 1] + (1 if s[0] == t[j] else 0)
            T[0][j] %= 1000000007

        for i in range(1, m):
            for j in range(1, n):
                T[i][j]  = T[i - 1][j] + T[i][j - 1] - (0 if s[i] == t[j] else T[i - 1][j - 1])
                T[i][j] %= 1000000007

        return T[m - 1][n - 1]


    def square_subsequences(string):
        m = len(string)
        R = 0

        for i in range(1, m):
            R += count_square_subsequences(string[i:], string[:i])
            R %= 1000000007

        return R


    def main():
        T = int(input())

        for _ in range(T):
            print(square_subsequences(input()))


    if __name__ == "__main__":
        main()

'''

def count_square_subsequences(s, t):
    m       = len(s)
    n       = len(t)

    T       = [[0 for _ in range(n)] for _ in range(m)]
    T[0][0] = 1 if s[0] == t[0] else 0

    for i in range(1, m):
        T[i][0]  = T[i - 1][0]
        T[i][0] %= 1000000007

    for j in range(1, n):
        T[0][j]  = T[0][j - 1] + (1 if s[0] == t[j] else 0)
        T[0][j] %= 1000000007

    for i in range(1, m):
        for j in range(1, n):
            T[i][j]  = T[i - 1][j] + T[i][j - 1] + (0 if s[i] == t[j] else -T[i - 1][j - 1])
            T[i][j] %= 1000000007

    return T[m - 1][n - 1]


def square_subsequences(string):
    m = len(string)
    R = 0

    for i in range(1, m):
        R += count_square_subsequences(string[i:], string[:i])
        R %= 1000000007

    return R


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    for line in lines[1:]:
        print(square_subsequences(line))


if __name__ == "__main__":
    main(sys.argv[1:])

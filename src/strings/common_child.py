import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code: 

    def common_child(s, t):
        m = len(s)
        n = len(t)

        P = [0 for _ in range(n + 1)]
        C = [0 for _ in range(n + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    C[j] = P[j - 1] + 1
                else:
                    C[j] = max(C[j - 1], P[j])
            P = C
            if i < m:
                C = [0 for _ in range(n + 1)]

        return C[n]


    def main():
        print(common_child(input(), input()))


    if __name__ == "__main__":
        main()

'''


def common_child(s, t):
    m = len(s)
    n = len(t)

    P = [0 for _ in range(n + 1)]
    C = [0 for _ in range(n + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                C[j] = P[j - 1] + 1
            else:
                C[j] = max(C[j - 1], P[j])
        P = C
        if i < m:
            C = [0 for _ in range(n + 1)]

    return C[n]


def main(argv):
    lines = files.read_lines(argv[0])

    print(common_child(*lines))


if __name__ == "__main__":
    main(sys.argv[1:])

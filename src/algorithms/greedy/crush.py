import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def crush(N, M, V):
        A = [v[1] for v in sorted(V, key = lambda x: (x[0], -x[1]))]

        for i in range(1, 2 * M):
            A[i] = A[i - 1] + A[i]

        return sorted(A)[-1]


    def main():
        N, M = [int(i) for i in input().split()]

        V = []
        for _ in range(M):
            a, b, k = [int(i) for i in input().split()]
            V.append((a, k))
            V.append((b, -k))

        print(crush(N, M, V))


    if __name__ == "__main__":
        main()

'''

def crush(N, M, V):
    A = [v[1] for v in sorted(V, key = lambda x: (x[0], -x[1]))]

    for i in range(1, 2 * M):
        A[i] = A[i - 1] + A[i]

    return sorted(A)[-1]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, M  = lines[0]

    V     = []
    for a, b, k in lines[1:]:
        V.append((a, k))
        V.append((b, -k))

    print(crush(N, M, V))


if __name__ == "__main__":
    main(sys.argv[1:])

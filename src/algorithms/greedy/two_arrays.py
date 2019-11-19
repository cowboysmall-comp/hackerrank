import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def two_arrays(N, K, A, B):
        A.sort()
        B.sort(reverse = True)

        for i in range(N):
            if A[i] + B[i] < K:
                return 'NO'

        return 'YES'


    def main():
        T = int(input())

        for _ in range(T):
            N, K = [int(i) for i in input().split()]
            A    = [int(i) for i in input().split()]
            B    = [int(i) for i in input().split()]

            print(two_arrays(N, K, A, B))


    if __name__ == "__main__":
        main()

'''

def two_arrays(N, K, A, B):
    A.sort()
    B.sort(reverse = True)

    for i in range(N):
        if A[i] + B[i] < K:
            return 'NO'

    return 'YES'


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N, K = lines[(3 * i) + 1]
        A    = lines[(3 * i) + 2]
        B    = lines[(3 * i) + 3]

        print(two_arrays(N, K, A, B))


if __name__ == "__main__":
    main(sys.argv[1:])

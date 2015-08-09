import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def flowers(N, K, C):
        T = 0
        X = 0
        C.sort(reverse = True)

        while C:
            T += (X + 1) * sum(C[:K])
            X += 1
            C  = C[K:]

        return T


    def main():
        N, K = [int(i) for i in input().split()]
        C    = [int(i) for i in input().split()]

        print(flowers(N, K, C))


    if __name__ == "__main__":
        main()

'''

def flowers(N, K, C):
    T = 0
    X = 0
    C.sort(reverse = True)

    while C:
        T += (X + 1) * sum(C[:K])
        X += 1
        C  = C[K:]

    return T


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, K  = lines[0]
    C     = lines[1]

    print(flowers(N, K, C))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def toys(P, K):
        C = 0
        for p in sorted(P):
            K -= p
            if K < 0:
                break
            C += 1

        return C


    def main():
        N, K = [int(i) for i in input().split()]
        P    = [int(i) for i in input().split()]

        print(toys(P, K))


    if __name__ == "__main__":
        main()

'''

def toys(P, K):
    C = 0
    for p in sorted(P):
        K -= p
        if K < 0:
            break
        C += 1

    return C


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, K  = lines[0]
    P     = lines[1]

    print(toys(P, K))


if __name__ == "__main__":
    main(sys.argv[1:])

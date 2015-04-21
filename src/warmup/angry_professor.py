import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code:

    def angry_professor(K, C):
        return 'NO' if len([c for c in C if c <= 0]) >= K else 'YES'


    def main():
        T = int(input())

        for _ in range(T):
            N, K  = [int(val) for val in input().split()]
            C     = [int(val) for val in input().split()]
            print(angry_professor(K, C))


    if __name__ == "__main__":
        main()

'''


def angry_professor(K, C):
    return 'NO' if len([c for c in C if c <= 0]) >= K else 'YES'


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N, K  = lines[(2 * i) + 1]
        C     = lines[(2 * i) + 2]
        print(angry_professor(K, C))


if __name__ == "__main__":
    main(sys.argv[1:])

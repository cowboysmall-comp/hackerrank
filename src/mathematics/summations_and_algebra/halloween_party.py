import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def optimal_slices(K):
        half = K // 2
        return half * (K - half)


    def main():
        T = int(input())

        for _ in range(T):
            print(optimal_slices(int(input())))


    if __name__ == "__main__":
        main()

'''


def optimal_slices(K):
    half = K // 2
    return half * (K - half)


def main(argv):
    lines = files.read_ints(argv[0])
    T     = lines[0]

    for K in lines[1:]:
        print(optimal_slices(K))


if __name__ == "__main__":
    main(sys.argv[1:])

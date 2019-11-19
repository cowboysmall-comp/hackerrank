import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def minimum_draws(P):
        return P + 1


    def main():
        T = int(input())

        for _ in range(T):
            print(minimum_draws(int(input())))


    if __name__ == "__main__":
        main()

'''

def minimum_draws(P):
    return P + 1


def main(argv):
    ints = files.read_ints(argv[0])
    T    = ints[0]

    for P in ints[1:]:
        print(minimum_draws(P))


if __name__ == "__main__":
    main(sys.argv[1:])

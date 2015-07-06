import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:




    def main():
        N, I = [int(i) for i in input().split()]

        P = []
        for _ in range(I):
            P.append([int(i) for i in input().split()])

        print(journey_to_the_moon(N, P))


    if __name__ == "__main__":
        main()

'''


def bit_positions(V):
    I = 0
    C = set()

    while V:
        if V & 1:
            C.add(I)
        I  += 1
        V >>= 1

    return C


def subset_component(N, D):
    C = [bit_positions(d) for d in D]

    return C


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    N = lines[0][0]
    D = lines[1]

    print(subset_component(N, D))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from collections import defaultdict


'''
    submitted code: 

    def find(S):
        length = len(S)
        freq   = defaultdict(int)
        needs  = {}
        A      = []
        R      = S[::-1]

        for c in S:
            freq[c] += 1

        for c in freq:
            needs[c] = freq[c] / 2

        index = 0

        while len(A) < length / 2:
            minimum = -1

            while True:
                c = R[index]

                if needs[c] > 0 and (minimum < 0 or c < R[minimum]):
                    minimum = index

                freq[c] -= 1

                if freq[c] < needs[c]:
                    break

                index += 1

            for j in range(minimum + 1, index + 1):
                freq[R[j]] += 1

            needs[R[minimum]] -= 1
            A.append(R[minimum])

            index = minimum + 1

        return ''.join(A)


    def main():
        print(find(input()))


    if __name__ == "__main__":
        main()

'''


def find(S):
    length = len(S)

    freq   = defaultdict(int)
    needs  = {}

    A      = []
    R      = S[::-1]

    for c in S:
        freq[c] += 1

    for c in freq:
        needs[c] = freq[c] / 2

    index = 0

    while len(A) < length / 2:
        minimum = -1

        while True:
            c = R[index]

            if needs[c] > 0 and (minimum < 0 or c < R[minimum]):
                minimum = index

            freq[c] -= 1

            if freq[c] < needs[c]:
                break

            index += 1

        for j in range(minimum + 1, index + 1):
            freq[R[j]] += 1

        needs[R[minimum]] -= 1
        A.append(R[minimum])

        index = minimum + 1

    return ''.join(A)


def main(argv):
    print(find(files.read_line(argv[0])))


if __name__ == "__main__":
    main(sys.argv[1:])

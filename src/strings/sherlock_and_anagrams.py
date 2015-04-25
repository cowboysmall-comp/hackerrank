import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def anagramic_pairs(string):
        length = len(string)
        count  = defaultdict(int)

        def nCr(n, r):
            return n * (n - 1) // 2

        for k in range(1, length):
            for i in range(length - k + 1):
                count[''.join(sorted(string[i: i + k]))] += 1

        return sum(nCr(n, 2) for n in count.values() if n > 1)


    def main():
        T = int(input())

        for _ in range(T):
            print(anagramic_pairs(input()))


    if __name__ == "__main__":
        main()

'''


def anagramic_pairs(string):
    length = len(string)
    count  = defaultdict(int)

    def nCr(n, r):
        return n * (n - 1) // 2

    for k in range(1, length):
        for i in range(length - k + 1):
            count[''.join(sorted(string[i: i + k]))] += 1

    return sum(nCr(n, 2) for n in count.values() if n > 1)


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    for line in lines[1:]:
        print(anagramic_pairs(line))


if __name__ == "__main__":
    main(sys.argv[1:])

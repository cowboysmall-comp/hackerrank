import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def changes(string):
        length = len(string)

        if length % 2 == 1:
            return -1
        else:
            counter1 = defaultdict(int)
            counter2 = defaultdict(int)

            split    = length // 2
            string1  = string[:split]
            string2  = string[split:]

            for c in string1:
                counter1[c] += 1

            for c in string2:
                counter2[c] += 1

            return sum([max(counter1[c] - counter2[c], 0) for c in set([char for char in string1])])


    def main():
        T = int(input())

        for _ in range(T):
            print(changes(input()))


    if __name__ == "__main__":
        main()

'''


def changes(string):
    length = len(string)

    if length % 2 == 1:
        return -1
    else:
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)

        split    = length // 2
        string1  = string[:split]
        string2  = string[split:]

        for c in string1:
            counter1[c] += 1

        for c in string2:
            counter2[c] += 1

        return sum([max(counter1[c] - counter2[c], 0) for c in set([char for char in string1])])


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    for line in lines[1:]:
        print(changes(line))


if __name__ == "__main__":
    main(sys.argv[1:])

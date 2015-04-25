import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def deletions(string1, string2):
        counter1  = defaultdict(int)
        counter2  = defaultdict(int)

        for c in string1:
            counter1[c] += 1

        for c in string2:
            counter2[c] += 1

        return sum(abs(counter1[c] - counter2[c]) for c in (set([c for c in string1]) | set([c for c in string2])))


    def main():
        print(deletions(input(), input()))


    if __name__ == "__main__":
        main()

'''


def deletions(string1, string2):
    counter1  = defaultdict(int)
    counter2  = defaultdict(int)

    for c in string1:
        counter1[c] += 1

    for c in string2:
        counter2[c] += 1

    return sum(abs(counter1[c] - counter2[c]) for c in (set([c for c in string1]) | set([c for c in string2])))


def main(argv):
    lines = files.read_lines(argv[0])

    print(deletions(*lines))


if __name__ == "__main__":
    main(sys.argv[1:])

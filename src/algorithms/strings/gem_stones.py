import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def gem_stones(strings):
        length   = len(strings)
        elements = defaultdict(set)

        for i in range(length):
            for char in strings[i]:
                elements[char].add(i)

        return [key for key in elements if len(elements[key]) == length]


    def main():
        T = int(input())

        print(len(gem_stones([input() for _ in range(T)])))


    if __name__ == "__main__":
        main()

'''

def gem_stones(strings):
    length   = len(strings)
    elements = defaultdict(set)

    for i in range(length):
        for char in strings[i]:
            elements[char].add(i)

    return [key for key in elements if len(elements[key]) == length]


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    print(len(gem_stones(lines[1:])))


if __name__ == "__main__":
    main(sys.argv[1:])

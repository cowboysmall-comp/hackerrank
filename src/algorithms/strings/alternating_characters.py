import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def deletions(string):
        current   = string[0]
        deletions = 0

        for character in string[1:]:
            if character != current:
                current    = character
            else:
                deletions += 1

        return deletions


    def main():
        T = int(input())

        for _ in range(T):
            print(deletions(input()))


    if __name__ == "__main__":
        main()

'''


def deletions(string):
    current   = string[0]
    deletions = 0

    for character in string[1:]:
        if character != current:
            current    = character
        else:
            deletions += 1

    return deletions


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    for line in lines[1:]:
        print(deletions(line))


if __name__ == "__main__":
    main(sys.argv[1:])

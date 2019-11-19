import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def palindrome_anagram(string):
        counter = defaultdict(int)

        for char in string:
            counter[char] += 1
            counter[char] %= 2

        return len([val for val in counter.values() if val == 1]) <= 1


    def main():
        if palindrome_anagram(input()):
            print('YES')
        else:
            print('NO')


    if __name__ == "__main__":
        main()

'''

def palindrome_anagram(string):
    counter = defaultdict(int)

    for char in string:
        counter[char] += 1
        counter[char] %= 2

    return len([val for val in counter.values() if val == 1]) <= 1


def main(argv):
    line = files.read_line(argv[0])

    if palindrome_anagram(line):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main(sys.argv[1:])

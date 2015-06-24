import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def is_funny_string(string):
        length = len(string)

        for i in range(1, length):
            if abs(ord(string[i]) - ord(string[i - 1])) != abs(ord(string[length - i - 1]) - ord(string[length - i])):
                return False

        return True


    def main():
        T = int(input())

        for _ in range(T):
            if is_funny_string(input()):
                print('Funny')
            else:
                print('Not Funny')


    if __name__ == "__main__":
        main()

'''


def is_funny_string(string):
    length = len(string)

    for i in range(1, length):
        if abs(ord(string[i]) - ord(string[i - 1])) != abs(ord(string[length - i - 1]) - ord(string[length - i])):
            return False

    return True


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    for string in lines[1:]:
        if is_funny_string(string):
            print('Funny')
        else:
            print('Not Funny')


if __name__ == "__main__":
    main(sys.argv[1:])

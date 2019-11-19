import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def is_pangram(string):
        letters = set()

        for c in ''.join(string.split()).lower():
            letters.add(c)
            if len(letters) == 26:
                return True

        return False


    def main():
        if is_pangram(input()):
            print('pangram')
        else:
            print('not pangram')


    if __name__ == "__main__":
        main()

'''

def is_pangram(string):
    letters = set()

    for c in ''.join(string.split()).lower():
        letters.add(c)
        if len(letters) == 26:
            return True

    return False


def main(argv):
    if is_pangram(files.read_line(argv[0])):
        print('pangram')
    else:
        print('not pangram')


if __name__ == "__main__":
    main(sys.argv[1:])

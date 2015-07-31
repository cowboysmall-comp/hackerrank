import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def xor_and_sum(a, b):
        return -1


    def main():
        a = reversed(input())
        b = reversed(input())

        print(xor_and_sum(a, b))


    if __name__ == "__main__":
        main()

'''

def xor_and_sum(a, b):
    return -1


def main(argv):
    lines = files.read_lines(argv[0])
    a     = lines[0]
    b     = lines[1]

    print(xor_and_sum(a, b))


if __name__ == "__main__":
    main(sys.argv[1:])

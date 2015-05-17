import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code:

    def main():
        n = int(input())


    if __name__ == "__main__":
        main()

'''


def main(argv):
    lines = files.read_lines_of_ints(argv[0])


if __name__ == "__main__":
    main(sys.argv[1:])

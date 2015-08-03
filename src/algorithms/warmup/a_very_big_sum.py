import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def main():
        N = int(input())
        A = [int(i) for i in input().split()]

        print(sum(A))


    if __name__ == "__main__":
        main()

'''

def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    A     = lines[1]

    print(sum(A))


if __name__ == "__main__":
    main(sys.argv[1:])

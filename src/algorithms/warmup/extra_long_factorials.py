import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

import math


'''
    submitted code:

    def main():
        N = int(input())

        print(math.factorial(N))


    if __name__ == "__main__":
        main()

'''

def extra_long_factorials(N):
    return 


def main(argv):
    N = files.read_int(argv[0])

    print(math.factorial(N))


if __name__ == "__main__":
    main(sys.argv[1:])

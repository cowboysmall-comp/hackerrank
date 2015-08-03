import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def solve_me_first(a, b):
        return a + b


    def main():
        a = int(input())
        b = int(input())

        print(solve_me_first(a, b))


    if __name__ == "__main__":
        main()

'''

def solve_me_first(a, b):
    return a + b
    

def main(argv):
    lines = files.read_ints(argv[0])
    a     = lines[0]
    b     = lines[1]

    print(solve_me_first(a, b))


if __name__ == "__main__":
    main(sys.argv[1:])

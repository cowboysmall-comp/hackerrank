import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def lonely_integer(array):
        counter = defaultdict(int)
        
        for value in array:
            counter[value] += 1

        return [key for key in counter if counter[key] == 1][0]


    def main():
        input()
        print(lonely_integer(map(int, input().strip().split(" "))))


    if __name__ == '__main__':
        main()

'''

def lonely_integer(array):
    counter = defaultdict(int)
    
    for value in array:
        counter[value] += 1

    return [key for key in counter if counter[key] == 1][0]


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    array = lines[1]

    print(lonely_integer(array))


if __name__ == "__main__":
    main(sys.argv[1:])

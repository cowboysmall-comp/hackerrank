import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def count_elements(array):
        counter = [0 for _ in range(100)]

        for val in array:
            counter[val] += 1

        return counter


    def main():
        n  = int(input())
        ar = [int(i) for i in input().split()]

        print(' '.join(str(count) for count in count_elements(ar)))


    if __name__ == "__main__":
        main()

'''

def count_elements(array):
    counter = [0 for _ in range(100)]

    for val in array:
        counter[val] += 1

    return counter


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    n     = lines[0][0]
    ar    = lines[1]

    print(' '.join(str(count) for count in count_elements(ar)))


if __name__ == "__main__":
    main(sys.argv[1:])

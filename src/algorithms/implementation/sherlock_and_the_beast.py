import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def decent_number(N):
        i = 0

        while N >= 5 * i:
            if ((N - (5 * i)) % 3) == 0:
                j = (N - (5 * i)) // 3
                return '5' * (j * 3) + '3' * (i * 5)

            i += 1

        return '-1'


    def main():
        T = int(input())

        for i in range(T):
            print(decent_number(int(input())))


    if __name__ == "__main__":
        main()


    this is the site-suggested version (I prefer mine):

    def decent_number(N):
        i = 0
        j = 0

        while ((N - (5 * i)) % 3) != 0 and j >= 0:
            i += 1
            j  = (N - (5 * i)) // 3

        j = (N - (5 * i)) // 3

        if j < 0:
            return '-1'
        else:
            return '5' * (j * 3) + '3' * (i * 5)

'''

def decent_number(N):
    i = 0

    while N >= 5 * i:
        if ((N - (5 * i)) % 3) == 0:
            j = (N - (5 * i)) // 3
            return '5' * (j * 3) + '3' * (i * 5)

        i += 1

    return '-1'


def main(argv):
    lines = files.read_ints(argv[0])

    for line in lines[1:]:
        print(decent_number(line))


if __name__ == "__main__":
    main(sys.argv[1:])

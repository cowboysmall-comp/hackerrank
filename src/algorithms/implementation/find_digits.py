import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def count_digit_dividers(N):
        count = 0
        value = N

        while value:
            digit = value % 10

            if digit != 0 and N % digit == 0:
                count +=1

            value //= 10

        return count


    def main():
        T = int(input())

        for _ in range(T):
            print(count_digit_dividers(int(input())))


    if __name__ == "__main__":
        main()

'''


def count_digit_dividers(N):
    count = 0
    value = N

    while value:
        digit = value % 10

        if digit != 0 and N % digit == 0:
            count +=1

        value //= 10

    return count


def main(argv):
    lines = files.read_ints(argv[0])
    T     = lines[0]

    for N in lines[1:]:
        print(count_digit_dividers(N))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def split_digits(N, t = 10):
        digits = []
        value  = N

        if N == 0:
            digits.append(0)
        else:
            while value:
                digits.insert(0, value % t)
                value //= t

        return digits


    def count_digits(N):
        count = 0
        value = abs(N)

        if N == 0:
            count += 1
        else:
            while value:
                count  += 1
                value //= 10

        return count


    def kaprekar_numbers(p, q):
        numbers = []

        for i in range(p, q + 1):
            if sum(split_digits(i ** 2, 10 ** count_digits(i))) == i:
                numbers.append(i)

        return numbers


    def main():
        p       = int(input())
        q       = int(input())
        numbers = kaprekar_numbers(p, q)

        if numbers:
            print(' '.join(str(n) for n in numbers))
        else:
            print('INVALID RANGE')


    if __name__ == "__main__":
        main()

'''

def split_digits(N, t = 10):
    digits = []
    value  = N

    if N == 0:
        digits.append(0)
    else:
        while value:
            digits.insert(0, value % t)
            value //= t

    return digits


def count_digits(N):
    count = 0
    value = abs(N)

    if N == 0:
        count += 1
    else:
        while value:
            count  += 1
            value //= 10

    return count


def kaprekar_numbers(p, q):
    numbers = []

    for i in range(p, q + 1):
        if sum(split_digits(i ** 2, 10 ** count_digits(i))) == i:
            numbers.append(i)

    return numbers


def main(argv):
    lines   = files.read_ints(argv[0])
    p       = lines[0]
    q       = lines[1]

    numbers = kaprekar_numbers(p, q)

    if numbers:
        print(' '.join(str(n) for n in numbers))
    else:
        print('INVALID RANGE')


if __name__ == "__main__":
    main(sys.argv[1:])

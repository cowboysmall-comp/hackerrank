import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def prime_factors(M):
        factors = []
        factor  = 2

        while factor ** 2 < M:
            while M % factor == 0:
                M //= factor
                factors.append(factor)
            factor += 1

        if M > 1:
            factors.append(M)

        return factors


    def sum_digits(n):
        sigma = 0

        while n:
            sigma += n % 10
            n    //= 10

        return sigma


    def main():
        M = int(input())

        print(1 if (sum_digits(M) == sum([sum_digits(f) for f in prime_factors(M)])) else 0)


    if __name__ == "__main__":
        main()

'''

def prime_factors(M):
    factors = []
    factor  = 2

    while factor ** 2 < M:
        while M % factor == 0:
            M //= factor
            factors.append(factor)
        factor += 1

    if M > 1:
        factors.append(M)

    return factors


def sum_digits(n):
    sigma = 0

    while n:
        sigma += n % 10
        n    //= 10

    return sigma


def main(argv):
    M = files.read_int(argv[0])

    print(1 if (sum_digits(M) == sum([sum_digits(f) for f in prime_factors(M)])) else 0)


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code:

    def antipalindromic(slength, alength):
        mod    = 1000000007
        value  = alength
        value %= mod
        if slength > 1:
            value *= (alength - 1)
            value %= mod
            value *= pow(alength - 2, slength - 2, mod)
            value %= mod
        return value


    def main():
        T = int(input())

        for _ in range(T):
            print(antipalindromic(*[int(i) for i in input().split()]))


    if __name__ == "__main__":
        main()

'''


def antipalindromic(slength, alength):
    mod    = 1000000007
    value  = alength
    value %= mod
    if slength > 1:
        value *= (alength - 1)
        value %= mod
        value *= pow(alength - 2, slength - 2, mod)
        value %= mod
    return value

def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for line in lines[1:]:
        print(antipalindromic(*line))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files



def count_digits(N):
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
        print(count_digits(N))


if __name__ == "__main__":
    main(sys.argv[1:])

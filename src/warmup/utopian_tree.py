import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files



def grow(cycles):
    height = 1

    for i in range(cycles):
        if i % 2 == 0:
            height *= 2
        else:
            height += 1
            
    return height


def main(argv):
    values = files.read_ints(argv[0])

    for value in values[1:]:
        print(grow(value))


if __name__ == "__main__":
    main(sys.argv[1:])

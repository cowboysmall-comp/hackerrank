import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files



def service_lane(W, P):
    widths = []

    for i, j in P:
        widths.append(min(W[i:j + 1]))

    return widths


def main(argv):
    lines = files.read_lines_of_ints(argv[0])

    N, T  = lines[0]
    W     = lines[1]

    print('\n'.join(str(val) for val in service_lane(W, lines[2:])))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files

from collections import defaultdict



def cut_sticks(sticks):
    cuts = []

    while sticks:
        smin   = min(sticks)
        s1     = []

        for s in sticks:
            cut = s - smin
            if cut > 0:
                s1.append(cut)

        cuts.append(len(sticks))
        sticks = s1

    return cuts


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    array = lines[1]

    print('\n'.join(str(c) for c in cut_sticks(array)))


if __name__ == "__main__":
    main(sys.argv[1:])

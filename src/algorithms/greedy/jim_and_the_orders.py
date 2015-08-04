import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def main():
        N = int(input())

        O = []
        for i in range(1, N + 1):
            t, d = [int(j) for j in input().split()]
            O.append((t + d, i))

        print(' '.join(str(o[1]) for o in sorted(O)))


    if __name__ == "__main__":
        main()

'''

def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    O     = [(lines[i][0] + lines[i][1], i) for i in range(1, N + 1)]

    print(' '.join(str(o[1]) for o in sorted(O)))


if __name__ == "__main__":
    main(sys.argv[1:])

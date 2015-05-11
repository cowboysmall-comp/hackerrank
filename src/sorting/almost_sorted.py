import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code:

    def main():
        n     = int(input())
        d     = [-1] + [int(i) for i in input().split()] + [1000001]
        start = []
        end   = []

        rev   = False
        swap  = False
        srtd  = False

        def fits(start, end):
            return d[end - 1] <= d[start] <= d[end + 1]

        for i in range(1, len(d) - 1):
            if d[i] > d[i - 1] and d[i] > d[i + 1]:
                start.append(i)
            if d[i] < d[i - 1] and d[i] < d[i + 1]:
                end.append(i)

        if len(start) == 0 and len(end) == 0:
            srtd = True

        if len(start) == 1 and len(end) == 1:
            if fits(start[0], end[0]) and fits(end[0], start[0]):
                if 4 <= len(d) <= 5:
                    swap = True
                else:
                    rev  = True

        if len(start) == 2 and len(end) == 2:
            if fits(start[0], end[1]) and fits(end[1], start[0]):
                swap = True

        if srtd:
            print('yes')
        elif rev:
            print('yes')
            print('reverse %s %s' % (start[0], end[0]))
        elif swap:
            print('yes')
            print('swap %s %s' % (start[0], end[-1]))
        else:
            print('no')


    if __name__ == "__main__":
        main()

'''


def main(argv):
    lines   = files.read_lines_of_ints(argv[0])
    n       = lines[0][0]
    d       = [-1] + lines[1] + [1000001]
    start   = []
    end     = []

    rev     = False
    swap    = False
    srtd    = False

    def fits(start, end):
        return d[end - 1] <= d[start] <= d[end + 1]

    for i in range(1, len(d) - 1):
        if d[i] > d[i - 1] and d[i] > d[i + 1]:
            start.append(i)
        if d[i] < d[i - 1] and d[i] < d[i + 1]:
            end.append(i)

    if len(start) == 0 and len(end) == 0:
        srtd = True

    if len(start) == 1 and len(end) == 1:
        if fits(start[0], end[0]) and fits(end[0], start[0]):
            if 4 <= len(d) <= 5:
                swap = True
            else:
                rev  = True

    if len(start) == 2 and len(end) == 2:
        if fits(start[0], end[1]) and fits(end[1], start[0]):
            swap = True

    if srtd:
        print('yes')
    elif rev:
        print('yes')
        print('reverse %s %s' % (start[0], end[0]))
    elif swap:
        print('yes')
        print('swap %s %s' % (start[0], end[-1]))
    else:
        print('no')


if __name__ == "__main__":
    main(sys.argv[1:])

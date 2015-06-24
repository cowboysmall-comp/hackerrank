import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def main():
        n     = int(input())
        d     = [-1] + [int(i) for i in input().split()] + [1000001]

        increasing = 0
        decreasing = 0
        iindex     = 0
        dindex     = 0

        def fits(start, end):
            return d[end - 1] <= d[start] <= d[end + 1]

        for i in range(1, len(d) - 1):
            if d[i - 1] < d[i] > d[i + 1]:
                increasing += 1
                if not iindex:
                    iindex  = i
            if d[i - 1] > d[i] < d[i + 1]:
                decreasing += 1
                dindex      = i

        if increasing == 0 and decreasing == 0:
            print('yes')
            return

        if increasing == 1 and decreasing == 1:
            if fits(iindex, dindex) and fits(dindex, iindex):
                print('yes\n%s %s %s' % ('swap' if dindex - iindex <= 2 else 'reverse', iindex, dindex))
                return

        if increasing == 2 and decreasing == 2:
            if fits(iindex, dindex) and fits(dindex, iindex):
                print('yes\n%s %s %s' % ('swap', iindex, dindex))
                return

        print('no')


    if __name__ == "__main__":
        main()

'''


def main(argv):
    lines      = files.read_lines_of_ints(argv[0])
    n          = lines[0][0]
    d          = [-1] + lines[1] + [1000001]

    increasing = 0
    decreasing = 0
    iindex     = 0
    dindex     = 0

    def fits(start, end):
        return d[end - 1] <= d[start] <= d[end + 1]

    for i in range(1, len(d) - 1):
        if d[i - 1] < d[i] > d[i + 1]:
            increasing += 1
            if not iindex:
                iindex  = i
        if d[i - 1] > d[i] < d[i + 1]:
            decreasing += 1
            dindex      = i

    if increasing == 0 and decreasing == 0:
        print('yes')
        return

    if increasing == 1 and decreasing == 1:
        if fits(iindex, dindex) and fits(dindex, iindex):
            print('yes\n%s %s %s' % ('swap' if dindex - iindex <= 2 else 'reverse', iindex, dindex))
            return

    if increasing == 2 and decreasing == 2:
        if fits(iindex, dindex) and fits(dindex, iindex):
            print('yes\n%s %s %s' % ('swap', iindex, dindex))
            return

    print('no')


if __name__ == "__main__":
    main(sys.argv[1:])

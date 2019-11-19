import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def counting_valleys(n, s):
        level = 0
        count = 0

        for c in s:
            if c == 'U':
                level += 1
                if level == 0:
                    count += 1
            else:
                level -= 1

        return count


    def main():
        n = int(input())
        s = input()

        print(counting_valleys(n, s))


    if __name__ == "__main__":
        main()

'''

def counting_valleys(n, s):
    level  = 0
    count  = 0

    for c in s:
        if c == 'U':
            level += 1
            if level == 0:
                count += 1
        else:
            level -= 1

    return count


def main(argv):
    n, s = files.read_lines(argv[0])

    print(counting_valleys(int(n), s))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def time_conversion(T):
        h  = int(T[:2])
        m  = int(T[3:5])
        s  = int(T[6:8])
        if T[8] == 'P' and h < 12:
            h += 12
        if T[8] == 'A' and h == 12:
            h = 0
        return '%02d:%02d:%02d' % (h, m, s)


    def main():
        T = input()

        print(time_conversion(T))


    if __name__ == "__main__":
        main()

'''

def time_conversion(T):
    h  = int(T[:2])
    m  = int(T[3:5])
    s  = int(T[6:8])
    if T[8] == 'P' and h < 12:
        h += 12
    if T[8] == 'A' and h == 12:
        h = 0
    return '%02d:%02d:%02d' % (h, m, s)


def main(argv):
    T = files.read_line(argv[0])

    print(time_conversion(T))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def substring(A, B):
        return len(set([a for a in A]) & set([b for b in B])) > 0


    def main():
        T = int(input())

        for i in range(T):
            A = input()
            B = input()
            if substring(A, B):
                print('YES')
            else:
                print('NO')


    if __name__ == "__main__":
        main()

'''

def substring(A, B):
    return len(set([a for a in A]) & set([b for b in B])) > 0


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    for i in range(T):
        A = lines[(2 * i) + 1]
        B = lines[(2 * i) + 2]
        if substring(A, B):
            print('YES')
        else:
            print('NO')


if __name__ == "__main__":
    main(sys.argv[1:])

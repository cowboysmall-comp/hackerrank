import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def simple_text_editor(ops):
        S     = ''
        R     = []

        for op in ops:
            t = op.split()
            if t[0] == '1':
                R.append(S)
                S += t[1]
            elif t[0] == '2':
                R.append(S)
                S = S[:-int(t[1])]
            elif t[0] == '3':
                print(S[int(t[1]) - 1])
            else:
                S = R.pop()


    def main():
        Q   = int(input())
        ops = [input() for _ in range(Q)]

        simple_text_editor(ops)


    if __name__ == "__main__":
        main()

'''

def simple_text_editor(ops):
    S     = ''
    R     = []

    for op in ops:
        t = op.split()
        if t[0] == '1':
            R.append(S)
            S += t[1]
        elif t[0] == '2':
            R.append(S)
            S = S[:-int(t[1])]
        elif t[0] == '3':
            print(S[int(t[1]) - 1])
        else:
            S = R.pop()


def main(argv):
    lines = files.read_lines(argv[0])

    simple_text_editor(lines[1:])


if __name__ == "__main__":
    main(sys.argv[1:])

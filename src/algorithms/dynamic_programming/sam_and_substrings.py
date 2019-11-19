import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def main():
        S = input()
        L = len(S)
        D = [int(c) for c in S]

        O = D[0]
        T = D[0]

        for i in range(1, L):
            T  = (T * 10) + ((i + 1) * D[i])
            T %= 1000000007
            O += T
            O %= 1000000007

        print(O)


    if __name__ == "__main__":
        main()

'''

def main(argv):
    S = files.read_line(argv[0])
    L = len(S)
    D = [int(c) for c in S]

    O = D[0]
    T = D[0]

    for i in range(1, L):
        T  = (T * 10) + ((i + 1) * D[i])
        T %= 1000000007
        O += T
        O %= 1000000007

    print(O)


if __name__ == "__main__":
    main(sys.argv[1:])

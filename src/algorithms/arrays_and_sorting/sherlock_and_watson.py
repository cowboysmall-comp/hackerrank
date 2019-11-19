import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def main():
        N, K, Q = [int(i) for i in input().split()]
        A       = [int(i) for i in input().split()]
        idx     = [int(input()) for _ in range(Q)]
        K      %= N

        print('\n'.join([str(A[(i - K + N) % N]) for i in idx]))


    if __name__ == "__main__":
        main()

'''

def main(argv):
    lines   = files.read_lines_of_ints(argv[0])
    N, K, Q = lines[0]
    A       = lines[1]
    idx     = [i[0] for i in lines[2:]]
    K      %= N

    print('\n'.join([str(A[(i - K + N) % N]) for i in idx]))


if __name__ == "__main__":
    main(sys.argv[1:])

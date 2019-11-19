import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


from collections import Counter


'''
    submitted code:

    def migratory_birds(arr):
        C = Counter(arr)
        F = sorted(list(zip(C.keys(), C.values())), key = lambda e: (-e[1], e[0]))

        return F[0][0]


    def main():
        n = int(input())
        a = list(map(int, input().rstrip().split()))

        print(migratory_birds(a))


    if __name__ == "__main__":
        main()

'''


def migratory_birds(arr):
    C = Counter(arr)
    F = sorted(list(zip(C.keys(), C.values())), key = lambda e: (-e[1], e[0]))

    return F[0][0]



def main(argv):
    n, arr = files.read_lines(argv[0])

    print(migratory_birds(map(int, arr.split())))


if __name__ == "__main__":
    main(sys.argv[1:])

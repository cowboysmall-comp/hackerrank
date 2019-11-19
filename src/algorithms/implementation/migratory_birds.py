import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def migratory_birds(arr):
        V = [0] * 5
        for a in arr:
            V[a - 1] += 1

        return V.index(max(V)) + 1


    def main():
        input()
        arr = list(map(int, input().rstrip().split()))

        print(migratory_birds(arr))


    if __name__ == "__main__":
        main()

'''


def migratory_birds(arr):
    V = [0] * 5
    for a in arr:
        V[a - 1] += 1

    return V.index(max(V)) + 1


def main(argv):
    n, arr = files.read_lines(argv[0])

    print(migratory_birds(map(int, arr.split())))


if __name__ == "__main__":
    main(sys.argv[1:])

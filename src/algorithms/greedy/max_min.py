import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def minimum_unfairness(array, K):
        array      = sorted(array)
        unfairness = []

        for i in range(len(array) - K + 1):
            unfairness.append(array[i + K - 1] - array[i])

        return min(unfairness)


    def main():
        N     = int(input())
        K     = int(input())

        array = []
        for i in range(N):
            array.append(int(input()))
        
        print(minimum_unfairness(array, K))


    if __name__ == "__main__":
        main()

'''

def minimum_unfairness(array, K):
    array      = sorted(array)
    unfairness = []

    for i in range(len(array) - K + 1):
        unfairness.append(array[i + K - 1] - array[i])

    return min(unfairness)


def main(argv):
    lines = files.read_ints(argv[0])
    N     = lines[0]
    K     = lines[1]

    print(minimum_unfairness(lines[2:], K))


if __name__ == "__main__":
    main(sys.argv[1:])

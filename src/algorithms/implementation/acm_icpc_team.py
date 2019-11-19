import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files

from collections import defaultdict


'''
    submitted code:

    def max_topics(array):
        counter = defaultdict(int)

        for i in range(len(array) - 1):
            for j in range(i + 1, len(array)):
                counter[bin(array[i] | array[j]).count('1')] += 1

        maximum = max(counter)
        return maximum, counter[maximum]


    def main():
        N, M   = [int(val) for val in input().split()]
        topics = [int(input(), 2) for _ in range(N)]

        print('\n'.join(str(value) for value in max_topics(topics)))


    if __name__ == "__main__":
        main()

'''

def max_topics(array):
    counter = defaultdict(int)

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            counter[bin(array[i] | array[j]).count('1')] += 1

    maximum = max(counter)
    return maximum, counter[maximum]


def main(argv):
    lines  = files.read_lines(argv[0])
    topics = [int(val, 2) for val in lines[1:]]

    print('\n'.join(str(value) for value in max_topics(topics)))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    (makes use of the following: http://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order)

    def greater_than(chars):
        chars  = [c for c in chars]
        length = len(chars)

        index1 = 0
        for i in range(length - 1, 0, -1):
            if ord(chars[i]) > ord(chars[i - 1]):
                index1 = i
                break

        if index1 == 0:
            return 'no answer'

        index2 = 0
        for j in range(length - 1, 0, -1):
            if ord(chars[j]) > ord(chars[index1 - 1]):
                index2 = j
                break

        chars[index1 - 1], chars[index2] = chars[index2], chars[index1 - 1]

        return ''.join(chars[:index1] + chars[index1:][::-1])


    def greater_than_alternate(chars):

        chars  = [c for c in chars]

        length = len(chars)
        index1 = length - 1
        index2 = length - 1

        while index1 > 0 and ord(chars[index1]) <= ord(chars[index1 - 1]):
            index1 -= 1

        if index1 == 0:
            return 'no answer'

        while ord(chars[index2]) <= ord(chars[index1 - 1]):
            index2 -= 1

        chars[index1 - 1], chars[index2] = chars[index2], chars[index1 - 1]

        return ''.join(chars[:index1] + chars[index1:][::-1])


    def main():
        T = int(input())

        for _ in range(T):
            print(greater_than(input()))


    if __name__ == "__main__":
        main()

'''


def greater_than(chars):
    chars  = [c for c in chars]
    length = len(chars)

    index1 = 0
    for i in range(length - 1, 0, -1):
        if ord(chars[i]) > ord(chars[i - 1]):
            index1 = i
            break

    if index1 == 0:
        return 'no answer'

    index2 = 0
    for j in range(length - 1, 0, -1):
        if ord(chars[j]) > ord(chars[index1 - 1]):
            index2 = j
            break

    chars[index1 - 1], chars[index2] = chars[index2], chars[index1 - 1]

    return ''.join(chars[:index1] + chars[index1:][::-1])


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    for line in lines[1:]:
        print(greater_than(line))


if __name__ == "__main__":
    main(sys.argv[1:])

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def deletion_index(string):
        length = len(string)

        for i in range(length):
            j = length - i - 1
            if string[i] != string[j]:
                s1 = string[:i] + string[i + 1:]
                if s1 == s1[::-1]:
                    return i
                else:
                    return j

        return -1


    def main():
        T = int(input())

        for _ in range(T):
            print(deletion_index(input()))


    if __name__ == "__main__":
        main()

'''

def deletion_index(string):
    length = len(string)

    for i in range(length):
        j = length - i - 1
        if string[i] != string[j]:
            s1 = string[:i] + string[i + 1:]
            if s1 == s1[::-1]:
                return i
            else:
                return j

    return -1


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    for line in lines[1:]:
        print(deletion_index(line))


if __name__ == "__main__":
    main(sys.argv[1:])

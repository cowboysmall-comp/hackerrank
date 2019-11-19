import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def palindrome(alpha, string):
        length = len(string)
        count  = 0

        for i in range(length // 2):
            val1 = alpha.index(string[i])
            val2 = alpha.index(string[length - i - 1])
            count += val2 - val1 if val2 > val1 else val1 - val2

        return count


    def main():
        alpha = [c for c in 'abcdefghijklmnopqrstuvwxyz']
        T     = int(input())

        for _ in range(T):
            print(palindrome(alpha, input()))


    if __name__ == "__main__":
        main()

'''

def palindrome(alpha, string):
    length = len(string)
    count  = 0

    for i in range(length // 2):
        val1 = alpha.index(string[i])
        val2 = alpha.index(string[length - i - 1])
        count += val2 - val1 if val2 > val1 else val1 - val2

    return count


def main(argv):
    alpha = [c for c in 'abcdefghijklmnopqrstuvwxyz']
    lines = files.read_lines(argv[0])

    for line in lines[1:]:
        print(palindrome(alpha, line))


if __name__ == "__main__":
    main(sys.argv[1:])

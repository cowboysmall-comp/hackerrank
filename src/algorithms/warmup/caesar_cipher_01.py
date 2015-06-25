import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def caesar_cipher(S, K):
        E = ''
        for s in S:
            c = ord(s)
            if 65 <= c <= 90:
                E += chr(65 + ((c - 65) + K) % 26)
            elif 97 <= c <= 122:
                E += chr(97 + ((c - 97) + K) % 26)
            else:
                E += s
        return E


    def main():
        N = int(input())
        S = input()
        K = int(input())

        print(caesar_cipher(S, K))


    if __name__ == "__main__":
        main()

'''


def caesar_cipher(S, K):
    E = ''
    for s in S:
        c = ord(s)
        if 65 <= c <= 90:
            E += chr(65 + ((c - 65) + K) % 26)
        elif 97 <= c <= 122:
            E += chr(97 + ((c - 97) + K) % 26)
        else:
            E += s
    return E


def main(argv):
    lines = files.read_lines(argv[0])
    N     = int(lines[0])
    S     = lines[1]
    K     = int(lines[2])

    print(caesar_cipher(S, K))


if __name__ == "__main__":
    main(sys.argv[1:])

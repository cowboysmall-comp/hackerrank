import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def pi_song(song, PI):
        A  = [len(word) for word in song.split()]

        for i in range(min(len(A), 29)):
            if A[i] != PI[i]:
                return 'It\'s not a pi song.'

        return 'It\'s a pi song.'


    def main():
        PI = [int(c) for c in '31415926535897932384626433833']
        T  = int(input())

        for _ in range(T):
            print(pi_song(input(), PI))


    if __name__ == "__main__":
        main()

'''

def pi_song(song, PI):
    A  = [len(word) for word in song.split()]

    for i in range(min(len(A), 29)):
        if A[i] != PI[i]:
            return 'It\'s not a pi song.'

    return 'It\'s a pi song.'


def main(argv):
    lines = files.read_lines(argv[0])
    PI    = [int(c) for c in '31415926535897932384626433833']
    T     = int(lines[0])

    for line in lines[1:]:
        print(pi_song(line, PI))


if __name__ == "__main__":
    main(sys.argv[1:])

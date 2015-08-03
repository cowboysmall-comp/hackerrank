import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def time_in_words(H, M):
        words = [
            'one', 'two', 'three', 'four', 'five', 
            'six', 'seven', 'eight', 'nine', 'ten', 
            'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 
            'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 
            'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 
            'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'half'
        ]
        if H > 12:
            H %= 12
        if M == 0:
            return '%s o\' clock' % (words[H - 1])
        else:
            if M <= 30:
                if M == 1:
                    return '%s minute past %s' % (words[M - 1], words[H - 1])
                elif M == 15 or M == 30:
                    return '%s past %s' % (words[M - 1], words[H - 1])
                else:
                    return '%s minutes past %s' % (words[M - 1], words[H - 1])
            else:
                M = 60 - M
                if M == 1:
                    return '%s minute to %s' % (words[M - 1], words[H])
                elif M == 15:
                    return '%s to %s' % (words[M - 1], words[H])
                else:
                    return '%s minutes to %s' % (words[M - 1], words[H])


    def main():
        H, M = int(input()), int(input())

        print(time_in_words(H, M))


    if __name__ == "__main__":
        main()

'''

def time_in_words(H, M):
    words = [
        'one', 'two', 'three', 'four', 'five', 
        'six', 'seven', 'eight', 'nine', 'ten', 
        'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 
        'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 
        'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 
        'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'half'
    ]
    if H > 12:
        H %= 12
    if M == 0:
        return '%s o\' clock' % (words[H - 1])
    else:
        if M <= 30:
            if M == 1:
                return '%s minute past %s' % (words[M - 1], words[H - 1])
            elif M == 15 or M == 30:
                return '%s past %s' % (words[M - 1], words[H - 1])
            else:
                return '%s minutes past %s' % (words[M - 1], words[H - 1])
        else:
            M = 60 - M
            if M == 1:
                return '%s minute to %s' % (words[M - 1], words[H])
            elif M == 15:
                return '%s to %s' % (words[M - 1], words[H])
            else:
                return '%s minutes to %s' % (words[M - 1], words[H])


def main(argv):
    H, M = files.read_ints(argv[0])

    print(time_in_words(H, M))


if __name__ == "__main__":
    main(sys.argv[1:])

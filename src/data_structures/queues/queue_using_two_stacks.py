import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def queue_using_two_stacks(queries):
        e = []
        d = []

        def pop():
            if not d:
                while e:
                    d.append(e.pop())
            return d.pop()

        for query in queries:
            t = query.split(' ')
            if t[0] == '1':
                e.append(t[1])
            elif t[0] == '2':
                pop()
            else:
                dd = pop()
                print(dd)
                d.append(dd)


    def main():
        q       = int(input())
        queries = [input() for _ in range(q)]

        queue_using_two_stacks(queries)


    if __name__ == "__main__":
        main()

'''

def queue_using_two_stacks(queries):
    e = []
    d = []

    def pop():
        if not d:
            while e:
                d.append(e.pop())
        return d.pop()

    for query in queries:
        t = query.split(' ')
        if t[0] == '1':
            e.append(t[1])
        elif t[0] == '2':
            pop()
        else:
            dd = pop()
            print(dd)
            d.append(dd)


def main(argv):
    lines = files.read_lines(argv[0])

    queue_using_two_stacks(lines[1:])


if __name__ == "__main__":
    main(sys.argv[1:])

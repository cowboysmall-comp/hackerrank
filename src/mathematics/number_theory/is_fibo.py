import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def fibonacci(N):
        fib = [0, 1]

        while fib[-1] < N:
            fib.append(fib[-1] + fib[-2])

        return fib


    def main():
        T = int(input())
        F = fibonacci(10 ** 10)

        for _ in range(T):
            if int(input()) in F:
                print('IsFibo')
            else:
                print('IsNotFibo')


    if __name__ == "__main__":
        main()

'''


def fibonacci(N):
    fib = [0, 1]

    while fib[-1] < N:
        fib.append(fib[-1] + fib[-2])

    return fib


def main(argv):
    lines = files.read_ints(argv[0])
    T     = lines[0]
    F     = fibonacci(10 ** 10)

    for N in lines[1:]:
        if N in F:
            print('IsFibo')
        else:
            print('IsNotFibo')


if __name__ == "__main__":
    main(sys.argv[1:])

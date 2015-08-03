import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../tools'))

import files


'''
    submitted code:

    def merge(A, B):
        m = len(A)
        n = len(B)
        i = 0 
        j = 0

        M = []

        while i < m and j < n:
            if A[i] < B[j]:
                M.append(A[i])
                i += 1
            elif A[i] > B[j]:
                M.append(B[j])
                j += 1
            else:
                ii = i
                jj = j

                c  = A[ii]
                while ii < m and jj < n and A[ii] == B[jj]:
                    if A[ii] > c:
                        M.append(A[i:ii])
                        M.append(B[j:jj])
                        i = ii
                        j = jj
                        c = A[ii]
                    ii += 1
                    jj += 1

                if ii == m:
                    M.append(B[j])
                    j += 1
                elif jj == n:
                    M.append(A[i])
                    i += 1
                else:
                    if A[ii] < B[jj]:
                        M.append(A[i])
                        i += 1
                    else:
                        M.append(B[j])
                        j += 1

        return ''.join(M) + A[i:] + B[j:]


    def main():
        T = int(input())

        for _ in range(T):
            A = input()
            B = input()
            print(merge(A, B))


    if __name__ == "__main__":
        main()



    A clean, but unusable solution - currently very slow and uses way 
    too much memory:

    def reverse_suffix_array(string):
        length = len(string)

        sa     = sorted([i for i in range(len(string))], key = lambda i: string[i:])
        rsa    = [0] * length

        for i in range(length):
            rsa[sa[i]] = i

        return rsa


    def merge(A, B):
        rsa = reverse_suffix_array(A + '~' + B + '~')

        m   = len(A)
        n   = len(B)
        i   = 0 
        j   = 0

        M   = []

        while i < m and j < n:
            if rsa[i] < rsa[m + j + 1]:
                M.append(A[i])
                i += 1
            else:
                M.append(B[j])
                j += 1

        return ''.join(M) + A[i:] + B[j:]



    Another solution - pretty slow:

    def merge(A, B):
        A += '~'
        B += '~'
        M  = []

        while len(A) > 1 and len(B) > 1:
            if A < B:
                M.append(A[0])
                A = A[1:]
            else:
                M.append(B[0])
                B = B[1:]

        return ''.join(M) + A[:-1] + B[:-1]


'''

def merge(A, B):
    m = len(A)
    n = len(B)
    i = 0 
    j = 0

    M = []

    while i < m and j < n:
        if A[i] < B[j]:
            M.append(A[i])
            i += 1
        elif A[i] > B[j]:
            M.append(B[j])
            j += 1
        else:
            ii = i
            jj = j

            c  = A[ii]
            while ii < m and jj < n and A[ii] == B[jj]:
                if A[ii] > c:
                    M.append(A[i:ii])
                    M.append(B[j:jj])
                    i = ii
                    j = jj
                    c = A[ii]
                ii += 1
                jj += 1

            if ii == m:
                M.append(B[j])
                j += 1
            elif jj == n:
                M.append(A[i])
                i += 1
            else:
                if A[ii] < B[jj]:
                    M.append(A[i])
                    i += 1
                else:
                    M.append(B[j])
                    j += 1

    return ''.join(M) + A[i:] + B[j:]


def main(argv):
    lines = files.read_lines(argv[0])
    T     = int(lines[0])

    for i in range(T):
        A = lines[(2 * i) + 1]
        B = lines[(2 * i) + 2]
        print(merge(A, B))


if __name__ == "__main__":
    main(sys.argv[1:])

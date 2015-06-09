import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files


'''
    submitted code:

    def maximize_sum(A, M):
        current = 0
        maximum = 0

        for a in A:
            current = max(0, (current + a) % M)
            maximum = max(maximum, current)

        return maximum


    def main():
        T = int(input())

        for _ in range(T):
            M = [int(i) for i in input().split()][1]
            A = [int(i) for i in input().split()]
            print(maximize_sum(A, M))


    if __name__ == "__main__":
        main()

'''


def maximize_sum(A, N, M):
    m = 0
    B = [0 for _ in range(N)]

    for i in range(N - 1):
        B[i] = A[i]
        for j in range(i + 1, N):
            B[j] = B[j - 1] + A[j]
            if m < B[j] % M:
                m = B[j] % M
            # else:
            #     break

    return m



def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    T     = lines[0][0]

    for i in range(T):
        N, M = lines[(2 * i) + 1]
        A    = lines[(2 * i) + 2]
        print(maximize_sum(A, N, M))
        # print(maximize_sum(A, M))
        # print(maximize_sum(A, M, 0, N - 1))


if __name__ == "__main__":
    main(sys.argv[1:])































# def maximize_sum(array):
#     current = 0
#     maximum = 0

#     # start   = 0
#     # end     = 0
#     pointer = 0

#     for index in range(len(array)):
#         if current < 0:
#             current  = array[index]
#             # pointer  = index
#         else:
#             current += array[index]

#         current = current 

#         if maximum < current:
#             maximum  = current
#             # start    = pointer
#             # end      = index

#     return maximum


# def maximize_sum(A, M):
#     current = 0
#     maximum = 0
#     # maxmod  = 0

#     for a in A:
#         current = max(0, current + (a % M))
#         maximum = max(maximum, current % M)
#         # maxmod  = max(maxmod, maximum % M)

#     return maximum


# def maximize_sum(A, N, M):
#     current = 0
#     maximum = 0

#     for index in range(N):
#         current += A[index]

#         if maximum < current % M:
#             maximum = current % M
#         else:
#             current = A[index] % M

#     return maximum



# def maximize_sum(A, M):
#     current = 0
#     maximum = 0

#     for a in A:
#         current = current + a

#         if maximum < current % M:
#             maximum = current % M
#         else:
#             current = a

#     return maximum


# def maximize_sum(A, N, M):
#     B = [A[0]] + [0 for _ in range(1, N)]
#     C = [A[0] % M] + [0 for _ in range(1, N)]

#     for i in range(1, N):
#         B[i] = B[i - 1] + A[i]
#         C[i] = B[i] % M

#     return B, C


# def maximize_sum(A, M, l, h):
#     if l > h:
#         return 0

#     if l == h:
#         return A[l] % M

#     m = (l + h) // 2

#     lmaximum = 0
#     current  = 0

#     for i in range(m, l - 1, -1):
#         # print(i)
#         current += A[i]
#         # current %= M
#         # lmaximum = max(lmaximum, current)
#         if lmaximum < current % M:
#             lmaximum = current % M
#         # else:
#         #     break

#     # print()
#     rmaximum = 0
#     current  = 0

#     for i in range(m + 1, h + 1):
#         # print(i)
#         current += A[i]
#         # current %= M
#         # rmaximum = max(rmaximum, current)
#         if rmaximum < current % M:
#             rmaximum = current % M
#         # else:
#         #     break

#     # current = 0
#     # maximum = 0

#     # for i in range(m, l - 1, -1):
#     #     current += A[i]
#     #     for j in range(m + 1, h + 1):


#     # print()

#     return max(lmaximum % M, rmaximum % M, (lmaximum + rmaximum) % M, maximize_sum(A, M, l, m), maximize_sum(A, M, m + 1, h))
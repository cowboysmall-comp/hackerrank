import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def largest_permutation(N, K, P):
        Q = [0 for _ in range(N + 1)]

        for i in range(N):
            Q[P[i]] = i

        for i in range(N):
            if K > 0:
                if P[i] != N - i:
                    j = Q[N - i]
                    P[i], P[j] = P[j], P[i]
                    Q[P[i]], Q[P[j]] = Q[P[j]], Q[P[i]]
                    K -= 1
            else:
                break

        return P


    def main():
        N, K = [int(i) for i in input().split()]
        P    = [int(i) for i in input().split()]

        print(' '.join(str(i) for i in largest_permutation(N, K, P)))


    if __name__ == "__main__":
        main()


    alternative implementation:

    def largest_permutation(N, K, P):
        Q = [i for i in range(N, 0, -1)]

        if P != sorted(P):
            for i in range(N):
                if K > 0:
                    if Q[i] != P[i]:
                        j  = P.index(max(P[i + 1:]))
                        P[i], P[j] = P[j], P[i]
                        K -= 1
                else:
                    break

        return P

'''

def largest_permutation(N, K, P):
    Q = [0 for _ in range(N + 1)]

    for i in range(N):
        Q[P[i]] = i

    for i in range(N):
        if K > 0:
            if P[i] != N - i:
                j = Q[N - i]
                P[i], P[j] = P[j], P[i]
                Q[P[i]], Q[P[j]] = Q[P[j]], Q[P[i]]
                K -= 1
        else:
            break

    return P


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N, K  = lines[0]
    P     = lines[1]

    print(' '.join(str(i) for i in largest_permutation(N, K, P)))


if __name__ == "__main__":
    main(sys.argv[1:])

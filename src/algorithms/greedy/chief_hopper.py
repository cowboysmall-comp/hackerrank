import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../../tools'))

import files


'''
    submitted code:

    def chief_hopper(N, H):

        def energy(E):
            for h in H:
                if h > E:
                    E -= h - E
                else:
                    E += E - h

                if E < 0:
                    return False

            return True

        def search(L, H):
            while L < H:
                M = L + (H - L) // 2
                if energy(M):
                    H = M
                else:
                    L = M + 1

            return L

        return search(0, 100000)


    def main():
        N = int(input())
        H = [int(i) for i in input().split()]

        print(chief_hopper(N, H))


    if __name__ == "__main__":
        main()

'''

def chief_hopper(N, H):

    def energy(E):
        for h in H:
            if h > E:
                E -= h - E
            else:
                E += E - h

            if E < 0:
                return False

        return True

    def search(L, H):
        while L < H:
            M = L + (H - L) // 2
            if energy(M):
                H = M
            else:
                L = M + 1

        return L

    return search(0, 100000)


def main(argv):
    lines = files.read_lines_of_ints(argv[0])
    N     = lines[0][0]
    H     = lines[1]

    print(chief_hopper(N, H))


if __name__ == "__main__":
    main(sys.argv[1:])

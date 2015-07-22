#include <vector>
#include <iostream>

using namespace std;


/*
    [ jerry@pantagruel hackerrank ] $ clang++ -O3 -msse2 -o substring_diff src/algorithms/dynamic_programming/substring_diff.cpp

    [ jerry@pantagruel hackerrank ] $ time ./substring_diff < data/algorithms/dynamic_programming/input/substring_diff_02.txt

    256
    13
    1500
    429
    752
    1191
    40
    13
    195
    1500

    real    0m0.397s
    user    0m0.338s
    sys     0m0.047s

*/


int maximum_length(string &P, string &Q, int S) {

    int m = P.length();

    vector< vector<int> > T(m, vector<int>(m));
    for(int i = 0; i < m; i++)
        for(int j = 0; j < m; j++)
            T[i][j] = P[i] != Q[j];

    int M = -1;
    for(int i = 0; i < m; i++) {

        if (m - i <= M)
            break;

        int fs1  =  0;
        int fs2  =  0;
        int bs1  =  0;
        int bs2  =  0;

        int ptr1 = -1;
        int ptr2 = -1;

        for(int j = 0; j < m - i; j++) {

            fs1 += T[j][i + j];
            fs2 += T[i + j][j];

            while (fs1 - bs1 > S) {

                ptr1++;
                bs1 += T[ptr1][i + ptr1];
            }

            while (fs2 - bs2 > S) {

                ptr2++;
                bs2 += T[i + ptr2][ptr2];
            }

            M = max(max(j - ptr1, j - ptr2), M);
        }
    }

    return M;
}


int main() {

    int    T;
    int    S;
    string P;
    string Q;

    cin >> T;

    for(int i = 0; i < T; i++) {

        cin >> S;
        cin >> P;
        cin >> Q;
        cout << maximum_length(P, Q, S) << endl;
    }
}

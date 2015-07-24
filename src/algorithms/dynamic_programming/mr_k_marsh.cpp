#include <vector>
#include <iostream>

using namespace std;


/*
    [ jerry@pantagruel hackerrank ] $ clang++ -O3 -msse2 -o mr_k_marsh src/algorithms/dynamic_programming/mr_k_marsh.cpp

    [ jerry@pantagruel hackerrank ] $ time ./mr_k_marsh < data/algorithms/dynamic_programming/input/mr_k_marsh_01.txt

    14

    real    0m0.003s
    user    0m0.004s
    sys     0m0.000s

*/


int perimeter(int M, int N, vector< vector<char> > &A) {

    vector< vector<int> > B(M + 1, vector<int>(N + 1, 0));
    vector< vector<int> > C(M + 1, vector<int>(N + 1, 0));

    for(int i = 0; i < M; i++)
        B[i][N] = N;

    for(int i = 0; i < N; i++)
        C[M][i] = M;


    for(int i = M - 1; i >= 0; i--) {

        for(int j = N - 1; j >= 0; j--) {

            B[i][j] = (A[i][j] == 'x') ? j : B[i][j + 1];
            C[i][j] = (A[i][j] == 'x') ? i : C[i + 1][j];
        }
    }


    int R = 0;
    for(int i = 0; i < M; i++)
        for(int j = 0; j < N; j++)
            if (A[i][j] == '.')
                for (int k = j + 1; k < B[i][j]; k++)
                    for (int l = i + 1; l < min(C[i][j], C[i][k]); l++)
                        if (B[l][j] > k)
                            R = max(R, 2 * (l - i) + 2 * (k - j));

    return R;
}


int main() {

    int M;
    int N;
    cin >> M >> N;

    vector< vector<char> > A(M, vector<char>(N));
    for(int i = 0; i < M; i++)
        for(int j = 0; j < N; j++)
            cin >> A[i][j];


    int R = perimeter(M, N, A);
    if (R > 0)
        cout << R << endl;
    else
        cout << "impossible" << endl;
}

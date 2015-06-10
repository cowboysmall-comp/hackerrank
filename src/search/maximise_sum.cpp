#include <set>
#include <vector>
#include <iostream>

using namespace std;


/*
    [ jerry@pantagruel hackerrank ] $ clang++ -O3 -msse2 -o maximise_sum src/search/maximise_sum.cpp

    [ jerry@pantagruel hackerrank ] $ time ./maximise_sum < data/search/input/maximise_sum_05.txt

    10001696897931
    10000550066646
    10000673751131
    10000968078477
    10000320856505

    real    0m0.720s
    user    0m0.683s
    sys     0m0.027s

*/


long long maximise_sum(vector<long long> & A, long long N, long long M) {

    set<long long> B;
    set<long long>::iterator I;

    B.insert(0);
    B.insert(M);

    long long S = 0;
    long long V = 0;

    for (long long i = 0; i < N; i++) {

        V += A[i];
        V %= M;

        I = B.lower_bound(V);
        while (*I == V)
            ++I;
        S = max(S, (V - *I + M) % M);

        B.insert(V);
    }

    return S;
}


int main() {

    long long T;
    long long N;
    long long M;

    cin >> T;

    for (long long i = 0; i < T; i++) {

        cin >> N >> M;

        vector<long long> A(N);
        for (long long j = 0; j < N; j++)
            cin >> A[j];

        cout << maximise_sum(A, N, M) << endl;
    }
}

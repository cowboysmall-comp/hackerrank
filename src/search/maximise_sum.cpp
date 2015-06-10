#include <set>
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

    real    0m1.138s
    user    0m1.041s
    sys     0m0.064s

*/


int main() {

    set<long long> B;
    set<long long>::iterator I;

    long long T;
    long long N;
    long long M;

    long long a;

    long long S;
    long long V;

    cin >> T;

    for (int i = 0; i < T; i++) {

        cin >> N >> M;

        B.insert(0);
        B.insert(M);

        S = 0;
        V = 0;

        for (int j = 0; j < N; j++) {

            cin >> a;

            V += a;
            V %= M;

            I = B.lower_bound(V);

            if (*I == V)
                ++I;

            S = max(S, (V - *I + M) % M);

            B.insert(V);
            B.insert(V + M);
        }

        cout << S << endl;

        B.clear();
    }
}

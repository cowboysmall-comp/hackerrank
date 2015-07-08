#include <vector>
#include <iostream>

using namespace std;


/*
    [ jerry@pantagruel hackerrank ] $ clang++ -O3 -msse2 -o subset_component src/algorithms/graph_theory/subset_component.cpp

    [ jerry@pantagruel hackerrank ] $ time ./subset_component < data/algorithms/graph_theory/input/subset_component_01.txt

    504

    real    0m0.002s
    user    0m0.000s
    sys     0m0.000s

*/


vector<int> set_positions(unsigned long long V) {

    vector<int> C(64);
    for (int i = 0; i < 64; i++) 
        C[i] = i;

    vector<int> P;
    int I = 0;

    while (V != 0) {

        if ((V & (unsigned long long) 1) != 0) {

            P.push_back(I);
            C[I] = P[0];
        }
        I++;
        V >>= 1;
    }

    return C;
}


int count_positions(vector<int> V) {

    int C = 0;

    for (int i = 0; i < 64; i++)
        if (i == V[i])
            C++;

    return C;
}


vector<int> combine_positions(vector<int> V, vector<int> W) {

    vector<int> C(64);

    for (int i = 0; i < 64; i++)
        C[i] = min(V[i], W[i]);

    return C;
}


int sum_subsets(vector< vector<int> > V, vector<int> M) {

    int S = count_positions(M);

    for (int i = 0; i < V.size(); i++)
        S += sum_subsets(vector< vector<int> >(V.begin() + i + 1, V.end()), combine_positions(M, V[i]));

    return S;
}


int main() {

    int N;
    cin >> N;

    vector< vector<int> > D;
    for (int i = 0; i < N; i++) {

        unsigned long long d;
        cin >> d;

        D.push_back(set_positions(d));
    }

    vector<int> M(64);
    for (int i = 0; i < 64; i++) 
        M[i] = i;

    cout << sum_subsets(D, M) << endl;
}

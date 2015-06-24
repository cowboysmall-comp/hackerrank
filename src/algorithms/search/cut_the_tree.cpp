#include <vector>
#include <iostream>

using namespace std;


/*
    [ jerry@pantagruel hackerrank ] $ clang++ -O3 -msse2 -o cut_the_tree src/search/cut_the_tree.cpp

    [ jerry@pantagruel hackerrank ] $ time ./cut_the_tree < data/search/input/cut_the_tree_04.txt

    90014

    real    0m0.217s
    user    0m0.200s
    sys     0m0.013s

*/

int dfs(vector<int> & X, vector< vector<int> > & G, vector<int> & V, int node) {

    X[node] += 1;

    for (int i = 0; i < G[node].size(); i++) {

        int n = G[node][i];
        if (X[n] == 0) {

            V[node] += dfs(X, G, V, n);
        }
    }

    return V[node];
}


int tree_diff(vector< vector<int> > & G, vector<int> & V, int N) {

    vector<int> X(N + 1);

    int root = 0;
    for (int i = 1; i < N + 1; i++) {

        if (G[i].size() > 1) {

            root = i;
            break;
        }
    }

    int T = dfs(X, G, V, root);
    int M = T;

    for (int i = 1; i < N + 1; i++) {

        M = min(M, abs(T - (2 * V[i])));
    }

    return M;
}


int main() {

    int N;
    cin >> N;

    vector<int> V(N + 1);
    for (int i = 1; i < N + 1; i++) {

        cin >> V[i];
    }

    int e0 = 0;
    int e1 = 0;
    vector< vector<int> > G(N + 1);
    for (int i = 1; i < N; i++) {

        cin >> e0 >> e1;
        G[e0].push_back(e1);
        G[e1].push_back(e0);
    }

    cout << tree_diff(G, V, N) << endl;
}

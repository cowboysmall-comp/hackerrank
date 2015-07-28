#include <vector>
#include <iostream>

using namespace std;


/*
    [ jerry@pantagruel hackerrank ] $ clang++ -O3 -msse2 -o floyd_city_of_blinding_lights src/algorithms/graph_theory/floyd_city_of_blinding_lights.cpp

    [ jerry@pantagruel hackerrank ] $ time ./floyd_city_of_blinding_lights < data/algorithms/graph_theory/input/floyd_city_of_blinding_lights_02.txt

    6
    -1
    0
    106

    real    0m0.005s
    user    0m0.000s
    sys     0m0.000s

*/


#define MAX 999999


void floyd(int N, vector< vector<int> > &G) {

    for (int k = 0; k < N; k++) {

        for (int i = 0; i < N; i++) {

            if (G[i][k] == MAX) 
                continue;

            int V = G[i][k];

            for (int j = 0; j < N; j++) {

                int W = G[k][j];

                if (G[i][j] > V + W)
                    G[i][j] = V + W;
            }
        }
    }
}


int main() {

    int N;
    int M;
    cin >> N >> M;

    vector< vector<int> > G(N, vector<int>(N, MAX));

    for (int n = 0; n < N; n++)
        G[n][n] = 0;

    int x;
    int y;
    int r;

    for (int i = 0; i < M; i++) {

        cin >> x >> y >> r;
        G[x - 1][y - 1] = r;
    }

    floyd(N, G);

    int Q;
    cin >> Q;

    int a;
    int b;
    for (int i = 0; i < Q; i++) {

        cin >> a >> b;
        int d = G[a - 1][b - 1];
        cout << (d == MAX ? -1 : d) << endl;
    }
}

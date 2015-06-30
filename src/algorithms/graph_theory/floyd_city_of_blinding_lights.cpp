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

    real    0m0.588s
    user    0m0.289s
    sys     0m0.276s

*/


#define MAX 99999


void floyd(int N, vector< vector<int> > &E) {

    for (int n = 1; n <= N; n++) {

        E[n][n] = 0;
    }

    for (int k = 1; k <= N; k++) {

        for (int i = 1; i <= N; i++) {

            if (E[i][k] != MAX) {

                for (int j = 1; j <= N; j++) {

                    if (E[k][j] != MAX) {

                        if (E[i][j] > E[i][k] + E[k][j]) { 

                            E[i][j] = E[i][k] + E[k][j];
                        }
                    }
                }
            }
        }
    }
}


int main() {

    int N;
    int M;
    cin >> N >> M;

    vector< vector<int> > E(N + 1, vector<int>(N + 1, MAX));

    int x;
    int y;
    int r;
    for(int i = 0; i < M; i++) {

        cin >> x >> y >> r;
        E[x][y] = r;
    }

    floyd(N, E);

    int Q;
    cin >> Q;

    int a;
    int b;
    for(int i = 0; i < Q; i++) {

        cin >> a >> b;
        cout << (E[a][b] == MAX ? -1 : E[a][b]) << endl;
    }
}

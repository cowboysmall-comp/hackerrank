#include <vector>
#include <iostream>

using namespace std;


/*
    [ jerry@pantagruel hackerrank ] $ clang++ -O3 -msse2 -o common_child src/strings/common_child.cpp

    [ jerry@pantagruel hackerrank ] $ time ./common_child < data/strings/common_child_05.txt

    1417

    real    0m0.120s
    user    0m0.111s
    sys     0m0.004s

*/


int common_child(string &s, string &t) {

    int m = s.length();
    int n = t.length();

    vector<int> P(n + 1, 0);
    vector<int> C(n + 1, 0);

    for(int i = 1; i < m + 1; i++) {

        for(int j = 1; j < n + 1; j++) {

            if (s[i - 1] == t[j - 1])
                C[j] = P[j - 1] + 1;
            else
                C[j] = max(C[j - 1], P[j]);
        }

        P = C;

        if (i < m)
            vector<int> C(n + 1, 0);
    }

    return C[n];
}


int main() {

    string s;
    string t;

    cin >> s;
    cin >> t;

    cout << common_child(s, t) << endl;
}

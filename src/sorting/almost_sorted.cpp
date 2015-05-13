#include <vector>
#include <iostream>

using namespace std;


/*
    [ jerry@pantagruel hackerrank ] $ clang++ -O3 -msse2 -o almost_sorted src/sorting/almost_sorted.cpp

    [ jerry@pantagruel hackerrank ] $ time ./almost_sorted < data/sorting/almost_sorted_01.txt 

    yes
    swap 1 2

    real    0m0.005s
    user    0m0.001s
    sys     0m0.002s

*/


bool fits(vector<int> & d, int start, int end) {

    return d[end - 1] <= d[start] && d[start] <= d[end + 1];
}


int main() {

    int n;
    cin >> n;

    vector<int> d(n + 2);
    d[0] = -1;
    for(int i = 1; i <= n; i++)
        cin >> d[i];
    d[n + 1] = 1000001;

    int increasing = 0;
    int decreasing = 0;

    int iindex     = 0;
    int dindex     = 0;

    for (int i = 1; i < n + 1; i++) {

        if (d[i - 1] < d[i] && d[i] > d[i + 1]) {

            increasing++;
            if (iindex == 0)
                iindex = i;
        }

        if (d[i - 1] > d[i] && d[i] < d[i + 1]) {

            decreasing++;
            dindex = i;
        }
    }

    if (increasing == 0 && decreasing == 0) {

        cout << "yes" << endl;
        return 0;
    } 

    if (increasing == 1 && decreasing == 1) {

        if (fits(d, iindex, dindex) && fits(d, dindex, iindex)) {

            if (dindex - iindex <= 2)
                cout << "yes\nswap" << " " <<  iindex << " " << dindex << endl;
            else
                cout << "yes\nreverse" << " " <<  iindex << " " << dindex << endl;
            return 0;
        }
    }

    if (increasing == 2 && decreasing == 2) {

        if (fits(d, iindex, dindex) && fits(d, dindex, iindex)) {

            cout << "yes\nswap" << " " <<  iindex << " " << dindex << endl;
            return 0;
        }
    }

    cout << "no" << endl;
}

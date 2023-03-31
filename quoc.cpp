#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, T; double s;
    s = 1 + 1 + 0.5;
    T = 2.0;
    int i = 3;
    while(T >= pow(10,-6))
    {
        T = T*i;
        s += 1/T;
        ++i;
        cout << "e(" << i <<")=" << fixed << setw(8) << setprecision(3) << s << endl;
       
    }
    return 0;
}


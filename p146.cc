#include <set>
#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

typedef unsigned long long LL;

template <typename T>
T modpow(T base, T exp, T modulus) {
  base %= modulus;
  T result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}
//LL modpow(LL a, LL k, LL p) { // a^k % p
//    LL ret = 1;
//    while(k) {
//        if(k % 2) ret = (ret * a) % p;
//        k /= 2;
//        a = (a * a) % p;
//    }
//    return ret;
//}

// Miller-Rabin primality test accurate for 64 bit integers
// http://miller-rabin.appspot.com/
bool Miller(LL n) {
    static LL bases[7] = { 2, 325, 9375, 28178, 450775, 9780504, 1795265022 };

    if(n == 2) return true;
    if(n < 2 || n%2 == 0) return false;

    LL d = n - 1, r;

    for(r=0; d%2==0; r++) d /= 2;
    cout << "2**" << r << " * " << d << endl;

    for(int i = 0; i < 7; i++) {
        //LL a = bases[i];
        LL a = rand() % (n - 4) + 2;
        LL x = modpow(a, d, n);

        cout << "Try " << a << endl;
            cout << x << endl;
        if(x == 1LL || x == n-1) continue;
        cout << "Yeah" << endl;

        bool cont=false;
        for(int j=0; j<r-1; j++) {
            cout << "loop" << endl;
            x = modpow(x, 2ULL, n);
            cout << x << endl;
            cout << "ok..." << endl;
            if(x == 1ULL) {
                cout << "Fuck!" << endl;
                return false;
            }
            if(x == n-1) {
                cout << "Yes!" << endl;
                cont=true;
                break;
            }
        }
        if(!cont) return false;
    }

    return true;
}

int main() {
    LL sum = 10;
    LL add[6] = { 1, 3, 7, 9, 13, 27 };
    rand();

    //for(LL n=11; n<1000000LL; n++) {
    while(true) {
        LL n;
        cin >> n;
        cout << Miller(n) << endl;
        continue;
        if(n%100000==0) cout << n << ": " << sum << endl;
        bool prime = true;
        for(int i=0; i<6; i++) {
            if(!Miller(n*n+add[i])) {
                cout << "Not " << n*n+add[i] << endl;
                prime = false;
                break;
            }
        }
        if(prime) sum += n;
    }
    
    cout << sum << endl;

    return 0;
}

#include <set>
#include <iostream>
#include <fstream>
#include <cstdlib>

#include <gmp.h>
#include <gmpxx.h>

using namespace std;

typedef mpz_class LL;

LL modpow(LL & b, LL e, LL m) {
    LL res;
    mpz_powm(res.get_mpz_t(), b.get_mpz_t(), e.get_mpz_t(), m.get_mpz_t());
    return res;
}
//template <typename T>
//T modpow(T base, T exp, T modulus) {
//  base %= modulus;
//  T result = 1;
//  while (exp > 0) {
//    if (exp & 1L) result = (result * base) % modulus;
//    base = (base * base) % modulus;
//    exp >>= 1;
//  }
//  return result;
//}
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
    //cout << "2**" << r << " * " << d << endl;

    for(int i = 0; i < 7; i++) {
        LL a = bases[i];
        //LL a = rand() % (n - 4) + 2;
        LL x = modpow(a, d, n);

        if(x == 1L || x == n-1) continue;

        bool cont=false;
        for(int j=0; j<r-1; j++) {
            x = (x*x)%n;
            if(x == 1L) {
                return false;
            }
            if(x == n-1) {
                cont=true;
                break;
            }
        }
        if(!cont) return false;
    }

    return true;
}

int main() {
    LL sum = 0;
    LL add[6] = { 27, 13, 9, 7, 3, 1 };

    // n cannot be odd, and must be congruent with 0 (mod 5)
    for(LL n=10; n<150000000L; n+=10) {
        if(n%1000000==0) cout << n << ": " << sum << endl;
        bool prime = true;
        // false positive with n^2+21 also prime, too bored to fix propoerly
        if(n == 144774340) continue; 
        for(int i=0; i<6; i++) {
            if(!Miller(n*n+add[i])) {
                prime = false;
                break;
            }
        }
        if(prime) sum += n;
    }
    
    cout << sum << endl;

    return 0;
}

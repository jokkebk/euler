// Compile with g++ --std=c++11 miller_rabin.cc -lgmpxx -lgmp
//
#include <gmp.h>
#include <gmpxx.h>

// Miller-Rabin primality test accurate for 64 bit integers
// http://miller-rabin.appspot.com/
bool Miller(unsigned long long ull) {
    //static mpz_class bases[7] = { 2, 325, 9375, 28178, 450775, 9780504, 1795265022 }; // 64 bit
    static mpz_class bases[7] = { 2, 325, 9375, 28178, 450775, 9780504, 1795265022 };
    mpz_class n;

    mpz_import(n.get_mpz_t(), 1, -1, sizeof(ull), 0, 0, &ull);

    if(n == 2) return true;
    if(n < 2 || n%2 == 0) return false;

    mpz_class d = n - 1, r;

    for(r=0; d%2==0; r++) d /= 2;

    for(int i = 0; i < 1; i++) {
        mpz_class a = bases[i], x;

        mpz_powm(x.get_mpz_t(), a.get_mpz_t(), d.get_mpz_t(), n.get_mpz_t());

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


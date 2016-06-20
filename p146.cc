#include <set>
#include <iostream>
#include <fstream>
#include <cstdlib>

#include <gmp.h>
#include <gmpxx.h>

using namespace std;

// Miller-Rabin primality test accurate for 64 bit integers
// http://miller-rabin.appspot.com/
bool Miller(unsigned long long ull) {
    static mpz_class bases[7] = { 2, 325, 9375, 28178, 450775, 9780504, 1795265022 };
    mpz_class n;

    mpz_import(n.get_mpz_t(), 1, -1, sizeof(ull), 0, 0, &ull);

    if(n == 2) return true;
    if(n < 2 || n%2 == 0) return false;

    mpz_class d = n - 1, r;

    for(r=0; d%2==0; r++) d /= 2;
    //cout << "2**" << r << " * " << d << endl;

    for(int i = 0; i < 7; i++) {
        //mpz_class a = rand() % (n - 4) + 2;
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

int main() {
    unsigned long long sum = 0, add[6] = { 27, 13, 9, 7, 3, 1 };

    // n cannot be odd, and must be congruent with 0 (mod 5)
    for(unsigned long long n=10; n<150000000ULL; n+=10) {
        if(n%1000000==0) cout << n << ": " << sum << endl;
        if((n*n+3) % 2 == 0) continue;
        if((n*n+27) % 3 == 0) continue;
        if((n*n+7) % 7 == 0) continue;
        if((n*n+13) % 7 == 0) continue;

        bool prime = true;

        for(int i=0; i<6; i++) {
            if(!Miller(n*n + add[i])) {
                prime = false;
                break;
            }
        }
        if(prime && !Miller(n*n+21)) sum += n;
    }
    
    cout << sum << endl;

    return 0;
}

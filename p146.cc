#include <set>
#include <iostream>
#include <cstddef>

#include <gmp.h>
#include <gmpxx.h>

using namespace std;

typedef long long LL;

bool isprime(LL ull) {
    static mpz_class two = 2;
    mpz_class n, n_1, x;

    mpz_import(n.get_mpz_t(), 1, -1, sizeof(ull), 0, 0, &ull);
    n_1 = n-1;
    mpz_powm(x.get_mpz_t(), two.get_mpz_t(), n_1.get_mpz_t(), n.get_mpz_t());
    return x == 1;
}

int main() {
    LL sum = 0, add[6] = { 27, 13, 9, 7, 3, 1 };
    set<LL> cand;

    // n cannot be odd, and must be congruent with 0 (mod 5)
    for(LL n=10; n<150000000LL; n+=10) {
        if((n*n+3) % 2 == 0) continue;
        if((n*n+27) % 3 == 0) continue;
        if((n*n+7) % 7 == 0) continue;
        if((n*n+13) % 7 == 0) continue;

        bool prime = true;

        for(int i=0; i<6; i++) {
            if(!isprime(n*n + add[i])) {
                prime = false;
                break;
            }
        }
        if(prime) cand.insert(n);
    }
    
    for(LL v : cand) {
        int c=0;
        for(LL i=1; i<=27; i++)
            if(isprime(v*v+i)) c++;
        if(c == 6) sum += v;
    }

    cout << sum << endl;

    return 0;
}

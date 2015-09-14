#include <iostream>
#include <set>
#include <map>
#include <list>
#include <utility>

using namespace std;

// Babylonian square check
bool square(long i) {
    if(i==1) return true;
    long x = i/2;
    set<long> seen;
    seen.insert(x);
    while(x*x != i) {
        x = (x + (i / x)) / 2;
        if(seen.count(x)) return false;
        seen.insert(x);
    }
    return true;
}

int main() {
    long N=2000;
    long n=N/2, a=0, b=1, c=1, d=n;
    map<long,list<long>> P;
    set<pair<long,long>> ok;
    set<long> done;

    while(c < n) {
        long k=(n+b)/d, a2=c, b2=d;
        c = k*c-a;
        d = k*d-b;
        a = a2;
        b = b2;
        if(square(a*a+b*b+a*b)) {
            for(long m=1; b*m<n; m++) {
                P[m*a].push_back(m*b);
                ok.insert(make_pair(m*a,m*b));
            }
        }
    }

    for(auto & x : P) {
        if(x.second.size() < 3) continue;
        cout << x.first << ": ";
        for(long v : x.second)
            cout << v << " ";
        cout << endl;
        continue;
        for(auto i=x.second.begin(); i!=x.second.end(); i++) {
            auto j=i;
            for(j++; j!=x.second.end(); j++) {
                cout << x.first << " " << *i << " " << *j << endl;
                break;
                if(ok.count(make_pair(*j,*i))) {
                    //cout << x.first << " " << *i << " " << *j << endl;
                    long s = x.first + *i + *j;
                    if(s<=N) done.insert(s);
                }
            }
        }
    }

    long S = 0;
    for(long s : done) S += s;
    cout << S << endl;

    return 0;
}

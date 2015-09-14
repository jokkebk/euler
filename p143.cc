#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

typedef long long LL;

bool square(LL n) {
    LL sq = (LL)sqrt(n);
    return sq*sq == n;
}

#define N 120000

int main() {
    LL a=0, b=1, c=1, d=N;
    map<LL,set<LL>> P;
    set<pair<LL,LL>> ok;
    set<LL> done;

    while(c < N) {
        LL k=(N+b)/d, a2=c, b2=d;
        c = k*c-a;
        d = k*d-b;
        a = a2;
        b = b2;
        if(square(a*a+b*b+a*b)) {
            for(LL m=1; b*m<N; m++) {
                P[m*a].insert(m*b);
                ok.insert(make_pair(m*a,m*b));
            }
        }
    }

    for(auto & x : P) {
        vector<LL> v(x.second.size());
        for(LL i : x.second) v.push_back(i);

        for(int i=0; i<v.size(); i++) {
            for(int j=i+1; j<v.size(); j++) {
                if(ok.count(make_pair(v[i],v[j]))) {
                    LL s = x.first + v[i] + v[j];
                    if(s<=N) done.insert(s);
                }
            }
        }
    }

    LL S = 0;
    for(LL s : done) S += s;
    cout << S << endl;

    return 0;
}

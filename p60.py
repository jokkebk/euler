import math, itertools, collections

def prime(n): return n not in poulet and pow(2, n-1, n) == 1
poulet = {}
with open('poulet.txt', 'r') as f:
    for s in f: poulet[int(s)] = True

primes = [p for p in range(2,8500) if prime(p)]
sets = set()
ok = {}

for a, b in itertools.product(primes, primes):
    if a < b and prime(int(str(a) + str(b))) and prime(int(str(b) + str(a))):
        ok[(a,b)] = ok[(b,a)] = True # quick lookup
        sets.add(frozenset([a,b]))

for i in range(3):
    comb = collections.defaultdict(set)
    for s in sets:
        ok[s] = True
        for v in s: comb[s - set([v])].add(v)

    sets = set() # next sets
    for key,sub in comb.items():
        for candi in itertools.combinations(sub, 2):
            if (candi in ok and (key | set([candi[0]])) in ok and
                    (key | set([candi[1]])) in ok):
                sets.add(key | set(candi))

print(min(sum(n for n in s) for s in sets))

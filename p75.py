triples = {}

for n in range(1, 900):
    for m in range(n+1, 900, 2): # step 1 generates mirrors
        (a,b,c) = (m*m-n*n, 2*m*n, m*m+n*n)
        for x in range(1, 1<<17):
            if x*(a+b+c) > 1500000: break
            triples.setdefault((a+b+c)*x, set()).add((x*a,x*b,x*c))

print(sum(1 for d in triples if len(triples[d]) == 1))

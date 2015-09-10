# We are looking for pythagorean triplets (k, 2k+-1, l)
# k = 2mn, 2k+-1 = m^2-n^2 = 4mn+-1 solved for m = 2n + sqrt(5n^2+-1)

def gen():
    sq = {i*i: i for i in range(1,1<<24)}
    for i in range(1,1<<24):
        try: yield (i, 2*i + sq[5*i*i+1])
        except: pass
        try: yield (i, 2*i + sq[5*i*i-1])
        except: pass

print(sum(m*m+n*n for n,m in gen()))

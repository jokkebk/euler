from itertools import product as p
print(min((abs(a*(a+1)*b*(b+1)//4-2e6),a*b) for a,b in p(range(80),range(80))))

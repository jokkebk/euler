from decimal import *
getcontext().prec = 102
print(sum(sum(int(c) for c in str(Decimal(n).sqrt()*Decimal(10**99)//1))\
        for n in range(1,101) if Decimal(n).sqrt()%1))

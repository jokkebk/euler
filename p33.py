def eq(m1,d1,m2,d2): return m1*d2 == m2*d1

def simpler(a,b):
    (a1,a2,b1,b2) = (a//10,a%10,b//10,b%10)
    if a2 == 0 and b2 == 0: return False
    if a1 == b1 and eq(a,b,a2,b2): return True
    if a2 == b2 and eq(a,b,a1,b1): return True
    if a1 == b2 and eq(a,b,a2,b1): return True
    if a2 == b1 and eq(a,b,a1,b2): return True
    return False

for a in range(11, 100):
    for b in range(11, 100):
        if a < b and simpler(a, b):
            print("%d/%d" % (a,b))

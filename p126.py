# Cuboid layers can be thought to replicate parts of basic 1x1x1 cuboid
# layers, with each side part repeated 4*l times and corner 8 times.
# Expansion can be thought as taxicab length measure from origin (0,0,0),
# so there will be 0, 1, 2, 3, .. cubes on side and (n-2)*(n-1)/2 cubes
# in corners. To illustrate, here is a 4z4x4 cube with taxicab measure>
#
# 3...  ....  ....  ....
# 23..  3...  ....  ....
# 123.  23..  3...  ....
# 0123  123.  23..  3...
#
# First row and column is the expansion of six planes of the cuboid, and
# sides include one 2s, two 3s, three 4s etc. Corners have 0, 1, 1+2,
# 1+2+3, .. cubes, so the total formula is>
#
# c(a,b,c,n) = 2(ab+ac+bc) + 4(n-1)(a+b+c) + 8(n-1)(n-2)/2
# = A + 4(n-1)(a+b+c + n-2)

C, N = {}, 20000

for a in range(1,N//4+1):
    for b in range(a, N):
        if 2*a*b > N: break
        for c in range(b, N):
            A, l = 2*(a*b+a*c+b*c), a+b+c
            if A > N: break
            for n in range(N):
                s = 4*n*(l+n-1)
                if A+s > N: break
                C[A+s] = C.setdefault(A+s, 0) + 1

print(min(n for n in C if C[n] == 1000))

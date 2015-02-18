def sol(p):
    for a in range(1,p//3):
        for b in range(a, p-a):
            c = p-a-b
            if a*a + b*b == c*c:
                yield (a,b,c)

def sols(n):
    return sum(1 for s in sol(n))

#print(max(len([s for s in sol(p)]) for p in range(3,1001)))

print(max((sols(i), i) for i in range(1,1001)))
#while True:
    #print(sols(int(input('> '))))

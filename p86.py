def gencubes(a,b): # a < b guaranteed, yield ordered triples
    for i in range(max(1,b-a), min(a,b//2+1)): yield (a,b-i,i) # split b
    for i in range(1,a//2+1): yield (b,a-i,i) # split a

# Generate cuboid rooms up to 2000 unit sides using pythagorean triplets
rooms = [set() for i in range(2000)] # longest side as index to enable search
for n in range(1, 500):
    for m in range(n+1, 500, 2): # step 1 generates mirrors
        (a,b,c) = (m*m-n*n, 2*m*n, m*m+n*n)
        if a > b: (a,b) = (b,a)
        for x in range(1, 2000//a+1):
            for r in gencubes(x*a,x*b):
                if r[0] < len(rooms): rooms[r[0]].add(r)

cubes = 0
for i,s in enumerate(rooms):
    cubes += len(s)
    if cubes > 1e6:
        print(i)
        break

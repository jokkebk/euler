ds = set()

for d in range(2, 12001):
    for n in range(int(d/3)+1, int(d/2)+1):
        ds.add(n/d)

print(len(ds)-1) # 1/2 is there

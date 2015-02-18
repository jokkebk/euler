from collections import Counter, defaultdict

num = Counter()
cubes = defaultdict(list)

for c in range(10000):
    s = "".join(sorted(str(c**3)))
    num[s] += 1
    cubes[s].append(c**3)

for tup in num.most_common(3):
    print(sorted(cubes[tup[0]]))

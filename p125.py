def pali(s): return all(s[i]==s[-1-i] for i in range(len(s)//2))

S = set()
for i in range(1,8000):
    s = i*i
    for j in range(i+1,8000):
        s += j*j
        if s > 10**8: break
        if pali(str(s)): S.add(s)

print(sum(S))

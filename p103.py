from itertools import combinations

def special(s):
    mid = (len(s)+1) // 2
    if sum(s[:mid]) <= sum(s[-(mid-1):]): return False

    for N in range(2,len(s)//2+1):
        sums = set()
        for sub in combinations(s, N):
            n = sum(sub)
            if n in sums: return False
            sums.add(n)

    return True

if __name__ == '__main__':
    for s in combinations(range(20,50), 7):
        if special(s): print(s, '=', sum(s))

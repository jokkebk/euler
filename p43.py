from itertools import permutations

divs = [2, 3, 5, 7, 11, 13, 17]

def iscool(s):
    for p, div in enumerate(divs):
        if int(s[p+1:p+4]) % div: return False
    return True

pans = ["".join(s) for s in permutations("0123456789")]
print(sum(int(s) for s in pans if iscool(s)))

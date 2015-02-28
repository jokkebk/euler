with open('p98.txt') as fin: words = fin.read().strip()
words = words[1:-1].split('","')

anagrams = {}
for w in words: anagrams.setdefault(''.join(sorted(w)), []).append(w)
anagrams = filter(lambda x: len(x)>1, anagrams.values())

sqlen = {}
for n in range(2,10**5): sqlen.setdefault(len(str(n*n)), []).append(n*n)

def key(word, square):
    m = {}
    for ch,n in zip(list(word), str(square)):
        if ch in m and m[ch] != n: return None
        m[ch] = n
    if len(set(m.values())) < len(m): return None # duplicate n's
    return hash(frozenset(m.items()))

hits = {}
for ws in anagrams:
    for word in ws:
        for sq in sqlen[len(word)]: # possible square matches
            hits.setdefault(key(word, sq), []).append((sq, word))

del hits[None]
print(max(max(pairs) for pairs in hits.values() if len(pairs) > 1))

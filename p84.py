from random import randint
from collections import namedtuple

sq = """GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3
FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2""".split()
S = namedtuple('S', sq)
s = S._make(range(len(sq)))

def CC(pos):
    if randint(0,7): return pos
    return s.GO if randint(0,1) else s.JAIL

def CH(pos):
    cards = [s.GO, s.JAIL, s.C1, s.E3, s.H2, s.R1, -1, -1, -2, (pos+37)%40]
    if pos == s.CH1: cards[6:8] = [s.R2, s.R2, s.U1]
    elif pos == s.CH2: cards[6:8] = [s.R3, s.R3, s.U2]
    else: cards[6:8] = [s.R1, s.R1, s.U1]
    return pos if randint(1,16) > 10 else cards[randint(0,10)]

handle = [lambda x: x] * 40
handle[s.G2J] = lambda x: s.JAIL
handle[s.CH1] = handle[s.CH2] = handle[s.CH3] = CH
handle[s.CC1] = handle[s.CC2] = handle[s.CC3] = CC

def advance(pos, cons):
    (a,b) = (randint(1,4), randint(1,4))
    pos = (pos + a + b) % 40 # go ahead
    cons = cons + 1 if a == b else 0 # count consecutive doubles
    if cons == 3: return(s.JAIL, 0) # go to jail, reset cons
    return (handle[pos](pos), cons)

(total, pos, cons) = ([0]*40, s.GO, 0) # clear counter, start at GO

for n in range(1000000): # number of repeats
    (pos, cons) = advance(pos, cons)
    total[pos] += 1

print(sorted(range(len(total)), key=lambda i: -total[i])[:3])

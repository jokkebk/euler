from collections import Counter

def analyze(hand):
    hand.sort()
    multi = Counter(value for value, suit in hand).most_common(2)
    flush = Counter(suit for value, suit in hand).most_common(1)[0][1] == 5
    straight = (multi[0][1] == 1) and ((hand[4][0] == hand[0][0] + 4) or
            (hand[3][0] == 5 and hand[4][0] == 14))
    ranks = []

    if flush and straight: # royal flush and straight flush
        ranks.append((9,0)) # straight ranking will sort out the rest

    if multi[0][1] == 4: # four of a kind
        ranks.append((8,multi[0][0]))

    if multi[0][1] == 3 and multi[1][1] == 3: # Full house
        ranks.append((7,0)) # triplet/pair ranking will sort out the rest

    if flush: ranks.append((6,0)) # straight / high card will handle the rest

    if straight:
        if hand[3][0] == 5 and hand[4][0] == 14:
            ranks.append((5,1)) # Ace is one
        else:
            ranks.append((5,hand[0][0]))
    
    if multi[0][1] == 3: # three of a kind (or full house, who cares)
        ranks.append((4,multi[0][0]))

    if multi[0][1] == 2: # two or three pairs
        if multi[1][1] == 2: # two pairs
            ranks.append((3,max(multi[0][0], multi[1][0])))
            ranks.append((3,min(multi[0][0], multi[1][0])))
        else: # one pair
            ranks.append((2,multi[0][0]))

    for value, suit in reversed(hand): ranks.append((1,value))
    while len(ranks) < 10: ranks.append((0,0)) # pad
    
    return tuple(ranks)

p1wins = 0
with open('p54_poker.txt', 'r') as f:
    for s in f:
        hand = [("23456789TJQKA".index(c[0]) + 2, c[1]) for c in s.split()]
        print(hand)
        if analyze(hand[:5]) > analyze(hand[5:]): p1wins += 1
        break
print(p1wins)

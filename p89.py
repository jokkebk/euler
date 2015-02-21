def from_roman(s):
    vals = [('IV', 4), ('IX', 9), ('XL', 40), ('XC', 90), ('CD', 400),
            ('CM', 900), ('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100),
            ('D', 500), ('M', 1000)]
    num = 0
    for ch,n in vals:
        while s.find(ch) != -1:
            num += n
            s = s.replace(ch, '', 1)
    return num

def to_roman(n):
    return "%s%s%s%s" % ("M"*(n//1000),
        ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'][(n//100)%10],
        ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'][(n//10)%10],
        ['','I','II','III','IV','V','VI','VII','VIII','IX'][n%10])

with open('p89.txt') as fin:
    print(sum(len(l.strip()) - len(to_roman(from_roman(l))) for l in fin))

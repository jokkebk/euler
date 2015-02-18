nums = []

with open('p79.txt') as fin:
    nums = [s.strip() for s in fin]

def isok(s):
    for n in nums:
        try:
            i = s.index(n[0])
            i = s.index(n[1], i+1)
            i = s.index(n[2], i+1)
        except: return False
    return True

for n in range(10000000, 100000000):
    if isok(str(n)):
        print(n)
        break

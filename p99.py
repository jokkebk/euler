from math import log

with open('p99.txt') as fin:
    be = [[int(i) for i in l.split(',')] for l in fin]

print(max(enumerate(be), key=lambda t: log(t[1][0])*t[1][1])[0] + 1)

def s(v,i,j): return (v[j]-v[i])*v[j+1] - (v[j+1]-v[i+1])*v[j] > 0

with open('p102.txt') as fin:
    vs = [[int(x) for x in line.split(',')] for line in fin]
    print(sum(1 for v in vs if s(v,0,2) == s(v,2,4) and s(v,0,2) == s(v,4,0)))

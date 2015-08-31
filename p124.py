rad = [1] * 1000001

for i in range(2,len(rad)):
    if rad[i] > 1: continue
    for j in range(i,len(rad),i):
        rad[j] *= i

print(sorted((rad[i], i) for i in range(1,100001))[9999][1])

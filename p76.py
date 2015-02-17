N = 100
ways = {(1,n): 1 for n in range(0, N+1)}

for num in range(2,N+1):
    for mul in range(0,N+1,num):
        for target in range(mul,N+1):
            if mul == 0:
                ways[(num, target)] = ways[(num-1, target)]
            else:
                ways[(num, target)] += ways[(num-1, target-mul)]
 
print(ways[(N-1, N)])

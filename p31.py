cur = [200, 100, 50, 20, 10, 5, 2]

def ways(sum, coin=0):
    if coin == len(cur): return 1
    num = 0
    for s in range(sum, -1, -cur[coin]):
        num += ways(s, coin+1)
    return num

print(ways(200))

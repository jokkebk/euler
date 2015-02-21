def generate(start, mul, add, terms):
    items = mul - add + terms
    if terms > 1 and items <= 12000:
        mins[items] = min(mins.setdefault(items, 1e6), mul)
    for n in range(start, 25000//mul):
        generate(n, mul*n, add+n, terms+1)

mins = {}
generate(2,1,0,0)
print(sum(set(mins.values())))

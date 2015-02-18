from functools import reduce
import operator

d = "".join([str(i) for i in range(200000)])
print(reduce(operator.mul, [int(d[10**i]) for i in range(7)], 1))

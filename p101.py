import numpy as np

def gen(n): return sum((-n)**p for p in range(11))
def calc(x,v): return sum((v**p)*a for p,a in enumerate(x))

def OP(n):
    a = [[(i+1)**p for p in range(n)] for i in range(n)]
    b = [gen(i+1) for i in range(n)]
    x = np.linalg.solve(np.array(a), np.array(b)).round()
    return next((calc(x,v) for v in range(1,12) if calc(x,v) != gen(v)), 0)

print(sum(OP(i) for i in range(1,12)))

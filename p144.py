inside = lambda x, y: 4*x*x+y*y <= 100

def coll(sx, sy, dx, dy):
    m = 0
    for p in range(32):
        m2 = m + 2**(-p)
        if inside(sx + dx * m2, sy + dy * m2): m = m2
    return (sx + dx*m, sy + dy*m)

def norm(x, y):
    l = (x*x + y*y)**0.5
    return (x/l, y/l)

sx, sy = 0, 10.1
dx, dy = 1.4, -19.7

for I in range(999):
    sx, sy = coll(sx, sy, dx, dy)
    if sy > 0 and abs(sx) <= 0.01:
        print(I)
        break
    mx, my = norm(1, -4*sx/sy)
    d = mx*dx + my*dy
    dx, dy = -dx + 2 * mx * d, -dy + 2 * my * d

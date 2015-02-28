(xk, yk) = (x1, y1) = (1, 1)

while True:
    (xk, yk) = (x1*xk+2*y1*yk, x1*yk+y1*xk)
    if xk>1e12 and xk&1 and yk&1:
        print((yk+1)//2)
        break

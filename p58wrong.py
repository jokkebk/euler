import math

prime = [True] * 100000000
for i in range(2,int(math.sqrt(len(prime)))):
    if not prime[i]: continue
    for j in range(i*2, len(prime), i):
        prime[j] = False
prime[1] = False

primes = 0
(x,y,dx,dy,val) = (0,0,1,0,1)
turns = [2, 3]

for i in range(len(prime)-1):
    (x, y, val) = (x + dx, y + dy, val + 1)

    if abs(x) == abs(y) and prime[val]: primes += 1

    if val == (2*x+1) * (2*y+1): # square end
        print("%d square: %d / %d = %f" % (
            2*x+1, primes, 4*x+1, primes/(4*x+1)))
        if primes/(4*x+1) < 0.1: break

    if val == turns[0]:
        (dx, dy) = (dy, -dx) # turn "left"
        if len(turns) == 2: # calculate next points
            d = turns[1] - turns[0] + 1
            turns.append(turns[1] + d)
            turns.append(turns[2] + d)
        turns.pop(0)

x = [7]
y = [5]

for i in range(13):
    print(x[-1], y[-1], x[-1]**2-2*y[-1]**2)
    if x[-1]%2 and y[-1]%2:
        (d,b) = ((x[-1]+1)//2, (y[-1]+1)//2)
        print(d, b, 1.0 * b*(b-1) / (d*(d-1)))
    x.append(x[0]*x[-1] + 2*y[0]*y[-1])
    y.append(x[0]*y[-1] + y[0]*x[-2])


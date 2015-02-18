n=lambda d:int(d*3/7)
print(min((3/7-n(d)/d,n(d)) for d in range(10**6+1) if 7*n(d)-3*d)[1])

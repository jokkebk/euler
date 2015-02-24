N = 20
semis = {n*(n-1): n for n in range(N)}

for d in range(N+1, 2*N+1):
    semi = d*(d-1)
    if semi//2 in semis:
        print(semi, semis[semi//2])
        break

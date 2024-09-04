N = []
prim = 0
for i in range(20):
    g = int(input())
    N.append(g)
for t in range(int(len(N)/2)):
    prim = N[t]
    N[t] = N[19-t]
    N[19-t] = prim
for p in range(len(N)):
    print(f"N[{p}] = {N[p]}")
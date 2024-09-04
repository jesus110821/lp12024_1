N, C = list(map(int, input().split()))

pessoas = 0
passou = False

for i in range(N):
    S, E = list(map(int, input().split()))
    pessoas = pessoas + E
    pessoas = pessoas - S
    if pessoas > C:
        passou = True
if passou:
    print('S')
else:
    print('N')

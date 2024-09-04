num = float(input())
vet = []
for i in range(0, 100):
    vet.append(0)
vet[0] = num
for i in range (1, 100):
    vet[i] = vet[i-1]/2
for i in range (0, 100):
    print("N[%d] = %.4f" %(i, vet[i]))
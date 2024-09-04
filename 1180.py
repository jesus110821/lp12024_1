n = int(input())
lista = input()
vet = lista.split(" ")
menor = int(vet[0])
pos = 0
for i in range(0, n):
    vet[i] = int(vet[i])
    if vet[i] < menor:
        menor = vet[i]
        pos = i
print(f"Menor valor: {menor}")
print(f"Posicao: {pos}")
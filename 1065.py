cont = 0

for i in range(5):
    valor = int(input())
    if valor % 2 == 0:
        cont += 1
print(f'{cont} valores pares')
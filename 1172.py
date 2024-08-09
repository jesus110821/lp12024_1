lista = []
for i in range(10):
    lista.append(int(input()))
for i in range(len(lista)):
    if lista[i] <= 0:
        lista[i] = 1
    print(f'X[{i}] = {lista[i]}')
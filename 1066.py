cont_positivos = 0
cont_negativos = 0
cont_impares = 0
cont_pares = 0

for i in range(5):
    valor = int(input())
    if valor > 0:
        cont_positivos += 1
    elif valor < 0:
        cont_negativos += 1
    if valor % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1

print(f'{cont_pares} valor(es) par(es)')
print(f'{cont_impares} valor(es) impar(es)')
print(f'{cont_positivos} valor(es) positivo(s)')
print(f'{cont_negativos} valor(es) negativo(s)')

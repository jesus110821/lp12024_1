tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6, 7)

intercalado = []

tamanho_max = max(len(tupla1), len(tupla2))

for i in range(tamanho_max):
    if i < len(tupla1):
        intercalado.append(tupla1[i])
    if i < len(tupla2):
        intercalado.append(tupla2[i])

tupla_intercalada = tuple(intercalado)

print(tupla_intercalada)

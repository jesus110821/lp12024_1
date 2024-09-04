X = int(input())

frequencia = [0] * 101

linha = input().split()

for i in  range(len(linha)):
    nota = int(linha[i])
    frequencia[nota] += 1

maior = 0
posicao = 0

for j in range(len(frequencia)):
    if maior <= frequencia[j]:
        posicao = j
        maior = frequencia[j]
print(posicao)


# N = int(input())
#
# frequencia = [0] * 100
#
# nota_mais_frequente = -1
#
# lista = []
#
# for i in range(N):
#     lista.append(map(int,input().split()))
#
# for i in lista:
#     if i in lista:
#         frequencia[i] += 1
#     else:
#         frequencia[i] = 1
#
# for i in frequencia:
#     if frequencia[i] > nota_mais_frequente:
#         nota_mais_frequente = frequencia[i]
#
# print(nota_mais_frequente)

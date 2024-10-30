N = int(input())
vetor = []

lista = input().split()
for valor in lista:
    vetor.append(int(valor))

a = 0

for i in range(1, N):
    if vetor[i] < vetor[i-1]:
        a = i+1
        break
print(a)

# N = int(input())
# menor = 0
# vetor = []
# lista = input().split()
# for valor in lista:
#     vetor.append(int(valor))
# print(vetor)

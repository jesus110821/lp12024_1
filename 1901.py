N = int(input())
vet = []
for i in range(N):
    vet.append(list(map(int, input().split())))

borboleta = []
for sexo in range(N*2):
    i, j = map(int, input().split())
    borboleta.append(vet[i-1][j-1])
print(len(set(borboleta)))



# n = int(input())
# matriz = []
# for i in range(n):
#     linha = list(map(int,input().split()))
#     matriz.append(linha)
# visitas=[]
# for v in range(n*2):
#     i,j = map(int,input().split())
#     if matriz[i-j][j-i] not in visitas:
#         visitas.append(matriz[i-j][j-i])
# print(len(visitas))
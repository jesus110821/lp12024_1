entrada = input("Tuplas separadas por espaço: ")

parte1, parte2 = entrada.split()
tupla1 = tuple(map(int, parte1.split(',')))
tupla2 = tuple(map(int, parte2.split(',')))

resultado = []

tamanho_tupla1 = len(tupla1)
tamanho_tupla2 = len(tupla2)

if tamanho_tupla1 > tamanho_tupla2:
    maior_tamanho = tamanho_tupla1
else:
    maior_tamanho = tamanho_tupla2

for i in range(maior_tamanho):
    if i < tamanho_tupla1:
        resultado.append(tupla1[i])
    if i < tamanho_tupla2:
        resultado.append(tupla2[i])

resultado = tuple(resultado)

print(resultado)







# tupla1 = tuple(map(int,input("Digite a primeira tupla: ").split(',')))
# tupla2 = tuple(map(int,input("Digite a segunda tupla: ").split(',')))
#
# tupla1 = tuple(input("Digite a primeira tupla: ").split(','))
# tupla2 = tuple(input("Digite a segunda tupla: ").split(','))
#
# resultado = []
#
# tamanho_tupla1 = len(tupla1)
# tamanho_tupla2 = len(tupla2)
#
# if tamanho_tupla1 > tamanho_tupla2:
#     maior_tamanho = tamanho_tupla1
# else:
#     maior_tamanho = tamanho_tupla2
#
# for i in range(maior_tamanho):
#     if i < tamanho_tupla1:
#         resultado.append(tupla1[i])
#     if i <tamanho_tupla2:
#         resultado.append(tupla2[i])
#
#
# resultado = tuple(resultado)
# print(resultado)

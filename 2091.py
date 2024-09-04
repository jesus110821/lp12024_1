N = int(input())
while N != 0:
    linha = list(map(int, input().split()))
    pilha = []
    for item in linha:
        if item in pilha:
            pilha.remove(item)
        else:
            pilha.append(item)
    print(pilha[0])
    N = int(input())


# while True:
#
#     N = int(input())
#
#     if N == 0:
#         break
#
#     lista = []
#
#     elementos = map(int,input().split())
#     for num in elementos:
#         if num not in lista:
#             lista.append(num)
#         elif lista.count(num % 2) == 1:
#             lista.remove(num)
#     print(lista)

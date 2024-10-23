n = int(input())
for i in range(n):
    a, b = input().split()
    lista1 = len(b)
    lista2 = a[-lista1:]
    if lista2 == b:
        print("encaixa")
    elif len(a) < len(b):
        print("nao encaixa")
    else:
        print("nao encaixa")
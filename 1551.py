n = int(input())
alfabeto = list("abcdefghijklmnopqrstuvwyz")
cont = 0
cont2 = 0
for i in range(n):
    frase = list(input().split())
    for j in alfabeto:
        if alfabeto[j] in frase:
            cont+=1
        elif cont != 0:
            cont2+=1
        elif cont2 >= 26:
            print("frase completa")
        elif cont2 >=13 and cont2 < 26:
            print("frase quase completa")
        else:
            print("frase mal elaborada")
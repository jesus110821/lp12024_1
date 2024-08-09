inicio, fim = map(int,input().split())

if inicio < fim:
    jogo = fim - inicio
else:
    jogo = (fim+24) - inicio
print(f'O JOGO DUROU {jogo} HORA(S)')
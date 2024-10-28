palavras = ['inefável', 'grill', 'faz', 'batata', 'ruim', '.', 'A', 'exceção', 'é', 'quando', 'faz', 'um', 'salgado', 'saboroso']
palavra = []
for x in palavras:
    try:
        palavra.append(x[3])
    except IndexError:
        continue
print(''.join(palavra))

#Saída: flamengo :D
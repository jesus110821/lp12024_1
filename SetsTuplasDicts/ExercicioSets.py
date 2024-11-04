lista1 = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Ana"]
lista2 = ["Carlos", "Eduardo", "Fernanda", "Gabriel", "Ana"]

conjunto1 = set(lista1)
conjunto2 = set(lista2)
intersecao = conjunto1 & conjunto2
pessoas_ambas = len(intersecao)

pessoas_duplicadas = len(lista1) + len(lista2) - len(conjunto1) - len(conjunto2)

uniao = conjunto1 | conjunto2
total_distintas = len(uniao)

pessoas_apenas_uma = len(uniao) - pessoas_ambas

print(pessoas_ambas)
print(pessoas_duplicadas)
print(total_distintas)
print(pessoas_apenas_uma)


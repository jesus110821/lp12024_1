#1) Escreva um programa que transforma uma lista de tuplas em um dicionário que associa o primeiro componente de cada tupla ao segundo.
lista_tuplas = [('a', 1), ('b', 2), ('c', 3)]
dicionario = dict(lista_tuplas)
print(dicionario)

#2) Escreva um programa que transforma um dicionário em uma lista de tuplas, onde as tuplas são ordenadas pelo primeiro componente. Lembre-se da função sort().
dicionario = {'c': 3, 'a': 1, 'b': 2}
lista_tuplas = sorted(dicionario.items())
print(lista_tuplas)

#3)Escreva um programa que conta a quantidade de vogais em um string e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada.
string = "exemplo de string"
vogais = 'aeiou'
contagem_vogais = {vogal: string.count(vogal) for vogal in vogais if string.count(vogal) > 0}
print(contagem_vogais)



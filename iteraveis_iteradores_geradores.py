#criar um iterador
str = 'ABC'
iterador = iter(str)
#Qualquer iterável pode ser percorrido com laço
for i in iterador:
    print(i)
#0 função next só funciona em iterators
# print(next(iterador), next(iterador), next(iterador))
#Não podemos usar next em iteráveis
# next(str)
# Função que retorna um iterador
alunos = ['Alice','Bernardo','Carlos']
it = enumerate(alunos) # o retorno é um iterador
# print(next(it))
for i in it:
    print(i)
reverso = reversed(alunos) #iterador que começa do último elemento
for i in reverso:
    print(i)
#Criar um dicionário a partir de um iterador
dicionario = dict(it)
print(dicionario)
for i in it:
    print(i)

numeros = [1,2,3,4]
geradora = (i ** 2 for i in numeros)
combinacao = zip(numeros,geradora) #sempre percorrerá até o tamanho da menor coleção
for i in combinacao:
    print(i)
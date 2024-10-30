def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não permitida"

def concatenar_strings(str1, str2):
    return str1 + " " + str2

def inverter_string(s):
    return s[::-1]

def contar_vogais(s):
    vogais = 'aeiouAEIOU'
    return sum(1 for char in s if char in vogais)

def adicionar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

def remover_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista

def ordenar_lista(lista):
    return sorted(lista)

def contar_elementos(lista):
    return len(lista)

def acessar_dicionario(dicionario, chave):
    return dicionario.get(chave, "Chave não encontrada")

def adicionar_dicionario(dicionario, chave, valor):
    dicionario[chave] = valor
    return dicionario

def remover_dicionario(dicionario, chave):
    if chave in dicionario:
        del dicionario[chave]
    return dicionario

def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def verificar_positivo_negativo(numero):
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Zero"

# Exemplos de uso das funções
print(soma(5, 3))
print(subtracao(10, 4))
print(multiplicacao(6, 7))
print(divisao(8, 2))
print(concatenar_strings("Olá", "Mundo"))
print(inverter_string("Python"))
print(contar_vogais("Exemplo"))
print(adicionar_elemento([1, 2, 3], 4))
print(remover_elemento([1, 2, 3, 4], 3))
print(ordenar_lista([5, 2, 8, 1]))
print(contar_elementos([1, 2, 3, 4]))
print(acessar_dicionario({'nome': 'João', 'idade': 25}, 'idade'))
print(adicionar_dicionario({}, 'cidade', 'São Paulo'))
print(remover_dicionario({'nome': 'Ana', 'idade': 22}, 'idade'))
print(verificar_par_impar(7))
print(verificar_positivo_negativo(-10))

# 1) Crie uma lista dos quadrados de todos os números ímpares entre 1 e 10.
quadrados_impares = [x**2 for x in range(1, 11) if x % 2 != 0]
print("1) Resolução:", quadrados_impares)  # Saída: [1, 9, 25, 49, 81]

# 2) Listar todos os números de 1 a 107 que tenham o dígito 7.
numeros_com_7 = [x for x in range(1, 108) if '7' in str(x)]
print("2) Resolução:", numeros_com_7)  # Saída: [7, 17, 27, 37, 47, 57, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 87, 97, 107]

# 3) Contar o número de espaços em branco de uma frase.
frase = "Essa é uma frase com vários espaços"
espacos = sum([1 for letra in frase if letra == ' '])
print("3) Resolução:", espacos)  # Saída: 6

# 4) Crie uma lista de todas as consoantes de uma frase.
frase = "Esta é uma frase com várias consoantes."
consoantes = [letra for letra in frase if letra.lower() in "bcdfghjklmnpqrstvwxyz"]
print("4) Resolução:", consoantes)  # Saída: ['s', 't', 'm', 'f', 'r', 's', 'c', 'm', 'v', 'r', 's', 'c', 'n', 's', 'n', 't', 's']

# 5) Dada uma lista de temperaturas em graus Celsius, crie uma lista correspondente com as temperaturas em Fahrenheit (use a fórmula F = C * 9/5 + 32).
celsius = [0, 20, 30, 40, 100]
fahrenheit = [((temp * 9/5) + 32) for temp in celsius]
print("5) Resolução:", fahrenheit)  # Saída: [32.0, 68.0, 86.0, 104.0, 212.0]

# 6) Crie uma list comprehension que filtre todos os números primos de uma lista de números.
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primos = [x for x in numeros if eh_primo(x)]
print("6) Resolução:", primos)  # Saída: [2, 3, 5, 7, 11]

# 7) Dada uma string, crie uma list comprehension que remova todas as vogais da string.
string = "Remover as vogais dessa frase"
sem_vogais = ''.join([letra for letra in string if letra.lower() not in "aeiou"])
print("7) Resolução:", sem_vogais)  # Saída: "Rmvr s vgs dss frs."

# 8) Crie uma list comprehension que gere a tabuada do 7.
tabuada_7 = [7 * i for i in range(1, 11)]
print("8) Resolução:", tabuada_7)  # Saída: [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# 9) Use list comprehension para calcular o produto de duas matrizes 2x2.
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]

produto = [[sum(a * b for a, b in zip(linha, coluna)) for coluna in zip(*matriz2)] for linha in matriz1]
print("9) Resolução:", produto)  # Saída: [[19, 22], [43, 50]]

# 10) Dada uma lista de palavras, crie uma list comprehension que gere uma lista contendo apenas as palavras que são anagramas de uma palavra fornecida.
palavras = ["amor", "roma", "carro", "mar", "mora", "ramo"]
palavra_fornecida = "roma"
anagramas = [palavra for palavra in palavras if sorted(palavra) == sorted(palavra_fornecida)]
print("10) Resolução:", anagramas)  # Saída: ['amor', 'roma', 'mora', 'ramo']

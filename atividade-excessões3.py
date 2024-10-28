entrada = input("Digite uma lista de valores inteiros separados por vírgulas: ")
valores = entrada.split(',')
numeros = []

for valor in valores:
    try:
        numeros.append(int(valor))
    except ValueError:
        print(f"O valor '{valor}' não é um inteiro válido.")

print("Lista de números inteiros:", numeros)

#Saída: C:\Users\Jesus\Desktop\projetos\.venv\Scripts\python.exe C:\Users\Jesus\Desktop\projetos\lp12024_1\github\atividade-excessões3.py
# Digite uma lista de valores inteiros separados por vírgulas: 5, 6, 7, 4.6, 76, 55, 3
# O valor ' 4.6' não é um inteiro válido.
# Lista de números inteiros: [5, 6, 7, 76, 55, 3]
#
# Process finished with exit code 0

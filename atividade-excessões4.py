tentativas = 0

while tentativas < 3:
    try:
        valor = float(input("Digite um valor real: "))
        print("Valor aceito:", valor)
        break
    except ValueError:
        tentativas += 1
        print(f"Valor inválido. Tentativa {tentativas} de 3.")
else:
    print("Você excedeu o limite de tentativas.")

# Saída: C:\Users\Jesus\Desktop\projetos\.venv\Scripts\python.exe C:\Users\Jesus\Desktop\projetos\lp12024_1\github\atividade-excessões4.py
# Digite um valor real: g
# Valor inválido. Tentativa 1 de 3.
# Digite um valor real: f
# Valor inválido. Tentativa 2 de 3.
# Digite um valor real: h
# Valor inválido. Tentativa 3 de 3.
# Você excedeu o limite de tentativas.
#
# Process finished with exit code 0

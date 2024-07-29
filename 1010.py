[codigo, numero_pecas, valor_un] = input().split()
[codigo2, numero_pecas2, valor_un2] = input().split()

numero_pecas = (int(numero_pecas))
numero_pecas2 = (int(numero_pecas2))

valor_un = (float(valor_un))
valor_un2 = (float(valor_un2))

a = numero_pecas * valor_un
b = numero_pecas2 * valor_un2
soma = a + b

print(f"VALOR A PAGAR: R$ {soma:.2f}")


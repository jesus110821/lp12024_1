n = float(input())
nota = n // 100 # // é divisão inteira.
print(f'{nota} nota(s) de R$ 100.00')
nota = int(n % 100) // 50
print(f'{nota} nota(s) de R$50.00')
nota = int((n % 100) % 50) // 20
print(f'{nota} nota(s) de R$ 20.00')
nota = int(((n % 100) % 50) % 20) // 10
print(f'{nota} nota(s) de R$10.00')
nota = int((((n % 100) % 50) % 20) % 10) // 5
print(f'{nota} nota(s) de R$ 5.00')
nota = int(((((n % 100) % 50) % 20) % 10) % 5) // 2
print(f'{nota} nota(s) de R$ 2.00')
moedas = int(((((n % 100) % 50) % 20) % 10) % 5 % 2)
print('MOEDAS:')
print(f'{moedas} moeda(s) de R$ 1.00)')
moedas = int(((((((n % 100) % 50) % 20) % 10) % 5) % 1) * 100) // 50
print(f'{moedas} moeda(s) de R$ 0.50)')
moedas = int(((((((n % 100) % 50) % 20) % 10) % 5) % 1) * 100) % 50
print(f'{moedas} moeda(s) de R$ 0.25)')
moedas = int(((((((((n % 100) % 50) % 20) % 10) % 5) % 1) * 100) % 50) % 25 // 10)
print(f'{moedas} moeda(s) de R$ 0.10)')
moedas = int(((((((((n % 100) % 50) % 20) % 10) % 5) % 1) * 100) % 50) % 25 // 10)

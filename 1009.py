nome = input()
salario = float(input())
total_vendas = float(input())

comissao = 0.15 * total_vendas

total_salario = salario + comissao

print(f'TOTAL = R$ {total_salario:.2f}')
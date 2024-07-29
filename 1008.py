num_empregado = int(input())
horas_trabalhadas = int(input())
valor_hora = float(input())

salary = horas_trabalhadas * valor_hora

print(f'NUMBER = {num_empregado}')
print(f'SALARY = U$ {salary:.2f}')
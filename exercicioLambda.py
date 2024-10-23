from functools import reduce

fatura = [('Net', 199.9), ('Ifood', 999.87), ('Gasolina', 678.0), ('Formigão', 400)]

formatado = map(lambda x: f"{x[0]} - R$ {x[1]:.2f}", fatura)
for item in formatado:
    print(item)

fatura_ordenada = sorted(fatura, key=lambda x: x[1])
print(fatura_ordenada)

gastos_acima_500 = filter(lambda x: x[1] > 500, fatura)
print(list(gastos_acima_500))

total_fatura = reduce(lambda x, y: x + y[1], fatura, 0)
print(f"Total da fatura: R$ {total_fatura:.2f}")

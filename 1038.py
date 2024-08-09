codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)

cachorro_quente = 4.00
x_salada = 4.50
x_bacon = 5.00
torrada_simples = 2.00
refrigerante = 1.50

if codigo == 1:
    print(f'Total: R$ {cachorro_quente * quantidade:.2f}')
elif codigo == 2:
    print(f'Total: R$ {x_salada * quantidade:.2f}')
elif codigo == 3:
    print(f'Total: R$ {x_bacon * quantidade:.2f}')
elif codigo == 4:
    print(f'Total: R$ {torrada_simples * quantidade:.2f}')
elif codigo == 5:
    print(f'Total: R$ {refrigerante * quantidade:.2f}')

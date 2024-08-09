num = int(input())
for i in range(1, num+1):
    num = int(input())
    cont = 0
    for j in range(1, num+1):
        if num % j == 0:
            cont += 1
    if cont == 2:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')
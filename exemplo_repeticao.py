n = int(input())
i = 1 #Contador
# soma = 0 #variavel acumuladora
status = False #variavel indicadora
ant = int(input())
while i <= n:
    x = int(input())
    if x < ant:
        status = True
    ant = x

    #soma = soma + 1
    i = i + 1
    # if i == 5:
    #     status = True
if status == False:
    print('crescente')
else:
    print('Não é crescente')
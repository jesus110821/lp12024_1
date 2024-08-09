cont = 0
nota1 = 0
nota2 = 0
while True:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        cont = cont + 1
        if cont == 1:
            nota1 = nota
        elif cont == 2:
            nota2 = nota
            media = (nota1+nota2)/2
            print(f"media = {media:.2f}")
            break
while True:
    try:
        s = input("Entre com um número: ")
        x = 5 / int(s) #O que imprime se digitar uma letra, 0 ou 2.5?
    except Exception:
        print('Programa interrompido.')
        break
    except ValueError:
        print(f"Número inválido! Tente novamente!")
    except ZeroDivisionError:
        print('Não existe divisão por zero. Tente novamente!')
    else:
        print(f'O resultado de 5/{s}: {x:.2f}')
    finally:
        print('Fim!')
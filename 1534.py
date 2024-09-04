while True:
    try:
        n = int(input())

        matriz = []
        for i in range(n):
            linha = ''
            for j in range(n):
                if i == j and i+j == n-1:
                    linha += '2'
                elif i == j:
                    linha += '1'
                elif i + j == n - 1:
                    linha += '2'
                else:
                    linha += '3'
            matriz.append(linha)

        for linha in matriz:
            print(linha)

    except EOFError:
        break

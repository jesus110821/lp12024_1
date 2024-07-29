x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())

raiz_quadrada = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
distancia = raiz_quadrada

print(f'{distancia:.4f}')
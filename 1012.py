a, b, c = map(float, input().split())
pi = 3.14159

triangulo_area = (a * c) / 2
circulo_area = pi * (c ** 2)
trapezio_area = ((a + b) * c) / 2
quadrado_area = b ** 2
retangulo_area = a * b

print(f"TRIANGULO: {triangulo_area:.3f}")
print(f"CIRCULO: {circulo_area:.3f}")
print(f"TRAPEZIO: {trapezio_area:.3f}")
print(f"QUADRADO: {quadrado_area:.3f}")
print(f"RETANGULO: {retangulo_area:.3f}")
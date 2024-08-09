A, B, C = map(float, input().split())

if A + B > C and A + C > B and C + B > A:
    print(f'Perimetro = {A + B + C}')
else:
    print(f'Area = {((A+B)*C)/2}')
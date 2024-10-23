def imprimir():
    print('Imprimir 1')
    yield 1
    print('Imprimir 2')
    yield 2
    print('Imprimir 3')
    yield 3

it = imprimir() #O retorno da função geradora é um iterador
print(it)
print(next(it), next(it), next(it))

def geradora():
    for i in range(10):
        yield i

it = geradora()
while  True:
    try:
        print(next(it))
    except StopIteration:
        break

MAXSIZE = 100100

vet = [0] * MAXSIZE

def bb(key, tam):
    low = 0
    hi = tam - 1

    while hi > low:
        mid = low + (hi - low) // 2
        if vet[mid] < key:
            low = mid + 1
        else:
            hi = mid

    return low

n = int(input())
numbers = input().split()
numbers = list(map(int, numbers))

soma = somatotal = 0
vet[0] = numbers[0]
somatotal += vet[0]

for i in range(1, n):
    tmp = numbers[i]
    vet[i] = vet[i - 1] + tmp
    somatotal += tmp

print(bb(somatotal // 2, n) + 1)

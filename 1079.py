N = int(input())
a, b, c = 0.0, 0.0, 0.0
media = 0.0
for g in range(N):
    a, b, c = map(float, input().split())
    media = (a * 2 + b * 3 + c * 5) / 10
    print(f"{media:.1f}")
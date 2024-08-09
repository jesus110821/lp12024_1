a, b, c = map(int, input().split())

if a <= b and a <= c:
    min_val = a
elif b <= a and b <= c:
    min_val = b
else:
    min_val = c

if a >= b and a >= c:
    max_val = a
elif b >= a and b >= c:
    max_val = b
else:
    max_val = c

if (min_val == b and max_val == c) or (min_val == c and max_val == b):
    meio_val = a
elif (min_val == a and max_val == c) or (min_val == c and max_val == a):
    meio_val = b
else:
    meio_val = c

print(min_val)
print(meio_val)
print(max_val)

print()

print(a)
print(b)
print(c)

a, b, c = map(int, input().split())

min = 101

if a <= b and a <= c:
    min = a
elif b <= a and b <= c:
    min = b
elif c <= a and c <= b:
    min = c

print(min)
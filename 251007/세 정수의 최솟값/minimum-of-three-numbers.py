a, b, c = map(int, input().split())

min = 101

if a <= b and b <= c:
    min = a
elif b <= a and b <= c:
    min = b
else:
    min = c

print(min)
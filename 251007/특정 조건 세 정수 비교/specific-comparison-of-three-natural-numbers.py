a, b, c = map(int, input().split())

min = 101

if a <= b and a <= c:
    min = a
elif b <= a and b <= c:
    min = b
else:
    min = c

if a == min:
    print(1, end=' ')
else:
    print(0, end=' ')

if a == b and b == c:
    print(1, end=' ')
else:
    print(0, end=' ')
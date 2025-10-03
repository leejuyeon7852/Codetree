a, b = map(int, input().split())

if max(a, b) == a:
    print(0, end=' ')
elif max(a, b) == b:
    print(1, end=' ')

if a == b:
    print(1, end=' ')
else:
    print(0, end=' ')



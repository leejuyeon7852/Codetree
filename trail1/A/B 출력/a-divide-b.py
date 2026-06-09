A, B = map(int, input().split())

print(A // B, end='.')

n = A % B
for i in range(20):
    n *= 10
    print(n // B, end='')
    n = n % B
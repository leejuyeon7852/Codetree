import sys

n = int(input())
a = [int(input()) for _ in range(n)]

total_d = 0
min_d = sys.maxsize


for i in range(n):
    d = 0
    total_d = 0
    for j in range(i, n+i):
        if d <= n:
            total_d += a[(j % n)-1] * d
            d += 1
            #print(f'j: {j}, j%n-1: {(j%n)-1}, {a[(j % n)-1]}')
    min_d = min(min_d, total_d)
    #print(f'total_d:{total_d}')

print(min_d)


import sys

INT_MAX = sys.maxsize

n = int(input())
A = list(map(int, input().split()))

total_d = 0
min_val = INT_MAX
for i in range(n):
    total_d = 0
    for j in range(n):
        total_d += A[j]*abs((j-i))
        #print(f'A[{j}]:{A[j]*(j-i)}, total: {total_d}')
    if total_d < min_val:
        min_val = total_d
        #print(f'min_val:{min_val}')    
print(min_val)   
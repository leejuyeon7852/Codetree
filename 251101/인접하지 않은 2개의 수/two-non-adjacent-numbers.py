import sys
n = int(input())
numbers = list(map(int, input().split()))

max_sum = -sys.maxsize

total = 0
for i in range(n):
    for j in range(i+2, n):
        total = numbers[i]+numbers[j]
        max_sum = max(max_sum, total)

print(max_sum)
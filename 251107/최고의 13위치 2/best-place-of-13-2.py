import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_count = 0
for i in range(n):
    for j in range(n):
        count = 0
        for k in range(j, j+3):
            if k < n and arr[i][k] == 1:
                count += 1
                max_count = max(max_count, count)
            if k + 3 < n and arr[i][k+3] == 1:
                count += 1
                max_count = max(max_count, count)
        for k in range(j, j+3):
            if k < n and i+1 < n and arr[i+1][k] == 1:
                count += 1
                max_count = max(max_count, count)
            
print(max_count)

        

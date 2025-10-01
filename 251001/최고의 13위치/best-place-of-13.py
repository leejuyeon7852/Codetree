n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n-2):
        count = max(count, grid[i][j] + grid[i][j+1] + grid[i][j+2])

print(count)
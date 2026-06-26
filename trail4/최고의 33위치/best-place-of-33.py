n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_coin = 0

for i in range(n-2):
    for j in range(n-2):
        total = 0
        for di in range(3):
            for dj in range(3):
                total += grid[i+di][j+dj]
        max_coin = max(max_coin, total)

print(max_coin)
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

x, y = 0, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

total = 0
for i in range(n):
    for j in range(n):
        x, y = i, j #좌표를 하나씩 꺼내서 
        count = 0
        for dx, dy in zip(dxs, dys): # 인접한 칸 계산
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                count += 1
        if count >= 3:
            total += 1
    
print(total)

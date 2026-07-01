n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

def explode_bomb(grid, r, c):
    r = r -1
    c = c - 1
    bomb = grid[r][c]
    
    grid[r][c] = 0 # 터트린 곳은 0

    for i in range(1, bomb):
       # 왼쪽 터트리기
        if c-i >= 0: 
            grid[r][c-i] = 0
        # 오른쪽 터트리기
        if c+i < n:  
            grid[r][c+i] = 0
        # 위쪽 터트리기
        if r - i >= 0: 
            grid[r-i][c] = 0
        # 아래쪽 터트리기
        if r + i < n:  
            grid[r+i][c] = 0

def drop_numbers(grid):
    temp = []
    for i in range(n):
        for j in range(n):
            if grid[j][i] != 0:
                temp.append(grid[j][i])
        
        for j in range(n):
            grid[j][i] = 0
        
        for j in range(n - 1, -1, -1):
            if temp:
                grid[j][i] = temp.pop()
            else:
                grid[j][i] = 0


explode_bomb(grid, r, c)
drop_numbers(grid)

for row in grid:
    print(*row) 
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

# 행 위치 찾기
def get_bomb_row(grid, col):
    for row in range(n):
        if grid[row][col] != 0:
            return row
    return -1 


def explode_bomb(grid, r, c):
    bomb_range = grid[r][c] 
    grid[r][c] = 0 

    for i in range(1, bomb_range):
        # 왼쪽 터뜨리기
        if c - i >= 0: 
            grid[r][c-i] = 0
        # 오른쪽 터뜨리기
        if c + i < n:  
            grid[r][c+i] = 0
        # 위쪽 터뜨리기
        if r - i >= 0: 
            grid[r-i][c] = 0
        # 아래쪽 터뜨리기
        if r + i < n:  
            grid[r+i][c] = 0


def drop_numbers(grid):
    for i in range(n): 
        temp = []
        for j in range(n):
            if grid[j][i] != 0:
                temp.append(grid[j][i])
        
        for j in range(n):
            grid[j][i] = 0
        
        for j in range(n - 1, -1, -1):
            if temp:
                grid[j][i] = temp.pop() 

for col_input in commands:
    col = col_input - 1 
    
    row = get_bomb_row(grid, col)

    if row != -1:
        explode_bomb(grid, row, col) 
        drop_numbers(grid)           

for row in grid:
    print(*row)
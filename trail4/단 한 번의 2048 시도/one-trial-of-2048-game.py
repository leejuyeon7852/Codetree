# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
d = input()

def push_left(row):
    temp = [n for n in row if n != 0]
    
    result = []
    i = 0
    while i < len(temp):
        if i+1 < len(temp) and temp[i] == temp[i+1]:
            result.append(temp[i]*2)
            i += 2
        else:
            result.append(temp[i])
            i += 1
        
    while len(result) < 4:
        result.append(0)
    
    return result

if d == "L":
    for row in range(4):
        grid[row] = push_left(grid[row])
elif d == "R":
    for row in range(4):
        reversed_row = grid[row][::-1]
        pushed_row = push_left(reversed_row)
        grid[row] = pushed_row[::-1]
elif d == "U":
    for col in range(4):
        vertical_row = [grid[row][col] for row in range(4)]
        pushed_row = push_left(vertical_row)
        for row in range(4):
            grid[row][col] = pushed_row[row]
else:
    for col in range(4):
        vertical_row = [grid[row][col] for row in range(3, -1, -1)]
        pushed_row = push_left(vertical_row)
        for i, row in enumerate(range(3, -1, -1)):
            grid[row][col] = pushed_row[i]

for i in range(4):
    for j in range(4):
        print(grid[i][j], end=' ')
    print()



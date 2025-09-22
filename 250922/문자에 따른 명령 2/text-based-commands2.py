dirs = input()
dirs = list(dirs)

MOVES = 4

x, y = 0, 0 # 기본값
dir_num = 3 #북
# 0-동, 1-남, 2-서, 3-북
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# 이동
for d in dirs:
    if d == 'L':
        dir_num = (dir_num-1 + MOVES) % MOVES
    elif d == 'R':
        dir_num = (dir_num + 1) % MOVES
    elif d == 'F':
        x, y = x+dx[dir_num], y+dy[dir_num]
    
print(x, y)


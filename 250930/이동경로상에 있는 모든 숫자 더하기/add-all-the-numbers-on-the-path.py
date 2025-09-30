N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# 시작
x, y = N//2, N//2

MOVES = 4
dir_num = 3 #북

# 0-동, 1-남, 2-서, 3-북
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

str = list(str)

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

sum = board[x][y]
for d in str:
    if d == 'L':
        dir_num = (dir_num - 1 + MOVES) % MOVES
        #print(f'L:{dir_num}')
    elif d == 'R':
        dir_num = (dir_num + 1) % MOVES
        #print(f'R: {dir_num}')
    elif d == 'F':
        #print(f'F: dir_num: {dir_num}, dx[{dir_num}]: {dx[dir_num]}')
        nx, ny = x+dx[dir_num], y+dy[dir_num]
        if in_range(nx, ny):
            x, y = nx, ny
            sum += board[x][y] 
            #print(f'F x:{x}, y:{y}, board[{x}][{y}]: {board[x][y]}, sum: {sum}')

print(sum)
  

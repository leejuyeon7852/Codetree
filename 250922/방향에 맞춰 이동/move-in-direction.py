class Move:
    def __init__(self, dir, dist):
        self.dir = dir
        self.dist = int(dist)
    def __str__(self):
        return f'({self.dir} {self.dist})'

n = int(input())
moves = []
for _ in range(n):
    dir, dist = input().split()
    moves.append(Move(dir, dist))

# 기본
x, y = 0, 0
# E-0, S-1, W-2, N-3
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# 최종 위치 찾기
dir_num = 0
for m in moves:
    if m.dir == 'E':
        dir_num = 0
    elif m.dir == 'S':
        dir_num = 1
    elif m.dir == 'W':
        dir_num = 2
    else:
        dir_num = 3
    for _ in range(m.dist):
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)

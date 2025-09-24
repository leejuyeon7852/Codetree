N = int(input())

x, y = 0, 0
MAX = 100
arr = [[0] * MAX for _ in range(MAX)]

# E-0, S-1, W-2, N-3
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

direction = {
    'E': 0, #동
    'S': 1, #남
    'W': 2, #서
    'N': 3 #북
}

time = 0
stop = False
for _ in range(N):
    dir, dist = input().split()
    dist = int(dist)
    dir_num = direction[dir]
    for _ in range(dist):
        time += 1
        x, y = x+dx[dir_num], y+dy[dir_num]
        if x == 0 and y == 0:
            stop = True
            break;
        #print(f'x:{x}, y:{y}, time: {time}')
    if stop:
        break;


if stop:
    print(time)
else:
    print(-1)



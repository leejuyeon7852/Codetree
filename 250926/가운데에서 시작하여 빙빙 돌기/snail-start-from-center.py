n = int(input())
grid = [[0] * n for _ in range(n)]

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]          
dir_num = 0           # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽

x, y = n//2, n//2
grid[x][y] = 1 #초기값 

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# n*n번 진행합니다.
for i in range(2, n*n+1):
    # 현재 방향 dir를 기준으로 그 다음 위치 값을 계산합니다.
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    # 더 이상 나아갈 수 없다면
    # 시계방향으로 90'를 회전합니다.
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4

    # 그 다음 위치로 이동한 다음 배열에 올바른 값을 채워넣습니다.
    x, y = x + dxs[dir_num], y + dys[dir_num]
    grid[x][y] = i

# 출력:
for i in range(n):
    for j in range(n):
        print(grid[i][j], end = ' ')
    print()
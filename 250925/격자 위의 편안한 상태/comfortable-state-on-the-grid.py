# 변수 선언 및 입력
n, m = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)] # N x N 크기 배열

# 동(0) 남(1) 서(2) 북(3) 
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] 

# 범위 확인
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

# 편안한 상태인지 확인하는 함수
def is_valid(x, y, arr): 
    count = 0
    for dir_num in range(4):
        nx, ny = x, y
        nx, ny = nx+dxs[dir_num], ny+dys[dir_num]
        #print(f'nx:{nx}, ny:{ny}, dir_num:{dir_num}')
        if in_range(nx, ny) and arr[nx][ny] == 1:
            count += 1
            #print(f'arr[{nx}][{ny}]:{arr[nx][ny]}, count:{count}')
    if count == 3:
        return 1 
    return 0

for _ in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    print(is_valid(x, y, arr))




n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c) # 처음 위치

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

# 방향 dict로 초기화 
direction = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}

def in_range(r, c):
    return 1 <= r and r <= n and 1 <= c and c <= n

dir_num = direction[d]

# T초 동안의 움직임
while t > 0:
    nr, nc = r+dxs[dir_num], c+dys[dir_num]
    if not in_range(nr, nc):
        dir_num = 3 - dir_num
        t -= 1
    # 이동
    r, c = r + dxs[dir_num], c + dys[dir_num]
    t -= 1
    #print(r, c)

print(r, c)




# 방향 입력
commands = input()
commands = list(commands)

# 동, 남, 서, 북 순으로 dx, dy를 정의합니다.
dxs = [1,  0, -1, 0]
dys = [0, -1,  0, 1]

x, y = 0, 0
curr_dir = 0
ans = -1
time = 0
# 움직이는 것을 진행합니다.
for command in commands:
    # 반시계방향 90' 회전
    if command == 'L':
        curr_dir = (curr_dir - 1 + 4) % 4
    # 시계방향 90' 회전
    elif command == 'R':
        curr_dir = (curr_dir + 1) % 4
    # 직진
    else:
        x, y = x + dxs[curr_dir], y + dys[curr_dir]
    time += 1
    if x == 0 and y == 0:
        ans = time
        break;

print(ans)



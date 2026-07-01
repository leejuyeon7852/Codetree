n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 우상향 (-1, 1), 좌상향(-1, -1), 좌하향(1, -1), 우하향(1, 1)
dxs = [-1, -1, 1, 1]
dys = [1, -1, -1, 1]

max_sum = 0

for r in range(n):
    for c in range(n):
        for w in range(1, n):
            for h in range(1, n):
                current_sum = 0
                cr, cc = r, c #현재 r, c 

                # 각 변의 길이와 이동 방향을 매칭
                # 0번 방향(우상)은 w칸, 1번 방향(좌상)은 h칸, 2번 방향(좌하)은 w칸, 3번 방향(우하)은 h칸
                move_counts = [w, h, w, h]
                is_possible = True
                
                for direction in range(4):
                    for _ in range(move_counts[direction]):
                        cr += dxs[direction]
                        cc += dys[direction]

                        if cr < 0 or cr >= n or cc < 0 or cc >= n:
                            is_possible = False
                            break
                        current_sum += grid[cr][cc]
                        
                    if not is_possible:
                        break
                    
                if is_possible:
                    max_sum = max(max_sum, current_sum)

print(max_sum)

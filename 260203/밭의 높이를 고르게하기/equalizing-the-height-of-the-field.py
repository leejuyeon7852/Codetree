N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# 비용 구하기
cost = [abs(H-x) for x in arr]

# 최소비용 합 T구간만큼 자르기
window = sum(cost[:T])
ans = window

for i in range(T, N):
    window += cost[i] - cost[i-T]
    ans = min(ans, window)

print(ans)
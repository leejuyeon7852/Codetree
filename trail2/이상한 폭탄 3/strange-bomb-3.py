N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

positions = {} # 폭탄들 위치 
for idx, n in enumerate(num):
    if n not in positions:
        positions[n] = []
    positions[n].append(idx)

exploded = [False] * N # 폭발 여부

for n, idx_list in positions.items():
    for i in range(len(idx_list)-1):
        if i+1 < len(idx_list):
            if idx_list[i+1]-idx_list[i] <= K:
                exploded[idx_list[i+1]] = True
                exploded[idx_list[i]] = True

count = {}
for i in range(N):
    if exploded[i]:
        value = num[i]
        if value not in count:
            count[value] = 0
        count[value] += 1

best_value = 0
best_count = 0

for value, cnt in count.items():
    if cnt > best_count or (cnt == best_count and value > best_value):
        best_count = cnt
        best_value = value

print(best_value)  
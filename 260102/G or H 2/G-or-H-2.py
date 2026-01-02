n = int(input())
people = [tuple(input().split()) for _ in range(n)]

people = [(int(p), ch) for p, ch in people]
# 정렬
people.sort(key=lambda x: x[0])

pos = [p for p, _ in people]
vals = [1 if ch == 'G' else -1 for _, ch in people]

prefix = 0
first_idx = {0: 0} # 누적합 : 누적합 처음 등장한 인덱스
ans = 0

for i in range(n):
    prefix += vals[i]
    idx = i+1

    if prefix not in first_idx:
        first_idx[prefix] = idx

    else:
        start = first_idx[prefix]      # 구간 시작 사람 인덱스
        end = idx - 1                  # 구간 끝 사람 인덱스
        # 구간 길이 = pos[end] - pos[start]
        ans = max(ans, pos[end] - pos[start])

print(ans)


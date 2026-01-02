n = int(input())
people = [tuple(input().split()) for _ in range(n)]
people = [(int(p), ch) for p, ch in people]
people.sort(key=lambda x: x[0])

pos = [p for p, _ in people]
alpha = [ch for _, ch in people]
vals = [1 if ch == 'G' else -1 for ch in alpha]

prefix = 0
first_idx = {0: 0}   # prefix 값이 처음 나온 "사람 인덱스"(0~n)
ans = 0

for i in range(n):
    prefix += vals[i]
    idx = i + 1  # prefix 인덱스(0~n)

    if prefix not in first_idx:
        first_idx[prefix] = idx
    else:
        start = first_idx[prefix]      # 구간 시작 사람 인덱스
        end = idx - 1                  # 구간 끝 사람 인덱스
        ans = max(ans, pos[end] - pos[start])

l = 0
for r in range(1, n):
    if alpha[r] != alpha[r - 1]:
        # [l, r-1] 구간은 같은 문자로만 구성
        ans = max(ans, pos[r - 1] - pos[l])
        l = r
ans = max(ans, pos[n - 1] - pos[l])

print(ans)

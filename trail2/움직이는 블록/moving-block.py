n = int(input())
blocks = [int(input()) for _ in range(n)]

avg = sum(blocks) // n
ans = 0
# 평균값에 근접하기 위해 필요한 값만 계산하면 됨
for e in blocks:
    if e > avg:
        ans += (e-avg)
print(ans)

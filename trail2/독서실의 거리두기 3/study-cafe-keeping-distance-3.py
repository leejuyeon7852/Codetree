N = int(input())
seats = input()

people = [p for p in range(len(seats)) if seats[p] == "1"]

n = len(people)

ans = 0
for i in range(n):
    if i+1 < n:
        left = people[i]
        right = people[i+1]
        mid = (left+right)//2
        diff = min(mid-left, right-mid)
        ans = max(ans, diff)

# 기존 최소 거리
if n == 1:
    print(ans)
else:
    min_existing = min(people[i+1] - people[i] for i in range(n-1))
    print(min(ans, min_existing))


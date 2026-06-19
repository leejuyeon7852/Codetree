N = int(input())
seat = input()

people = [] # 앉아있는 곳 인덱스 모음
for i in range(N):
    if seat[i] == "1":
        people.append(i)

n = len(people)

ans = 0
# 맨 왼쪽 끝
ans = max(ans, people[0]) 

for i in range(n):
    if i+1 < n:
        left = people[i]
        right = people[i+1]
        mid = (left+right)//2
        diff = min(mid-left, right-mid)
        ans = max(ans, diff)

# 오른쪽 끝과 비교
ans = max(ans, (N-1)-people[-1]) 

# 기존 최소 거리
if n == 1:
    print(ans)
else:
    min_existing = min(people[i+1] - people[i] for i in range(n-1))
    print(min(ans, min_existing))

        


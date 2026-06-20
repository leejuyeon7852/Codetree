n = int(input())
a = list(map(int, input().split()))

setA = set(a)
ans = 0
# print(setA)
count = 0

# 숫자가 하나밖에 없을 때
if len(setA) == 1: 
    ans = -1
elif len(setA) == 2 and n == 2: # 숫자 두개
    ans = a.index(max(a))
elif len(setA) == 2 and n != 2: # 숫자 두 개인데 중복되었다는 것 
    for i in range(n):
        if a[i] == max(setA):
            ans = i
            count += 1
    if count != 1: # 두 번째로 작은 수가 여러개
        ans = -1
else: # 숫자 여러개 
    pos = 0
    setB = set()
    for i in range(n):
        if min(a) < a[i] and a[i] < max(a): # 두 번째로 작은 수 찾기
            setB.add(a[i])
    # 중복인지 검사
    idx = a.index(min(setB))
    ans = idx
    for i in range(idx+1, n):
        if a[i] == min(setB):
            ans = -1
if ans >= 0:
    ans += 1
print(ans)
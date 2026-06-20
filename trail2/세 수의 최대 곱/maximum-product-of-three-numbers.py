n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

positive = [n for n in arr if n >= 0]
negative = [n for n in arr if n < 0]

candidates = []

# n이 3일 경우
if n == 3:
    multi = 1
    for i in range(n):
        multi *= arr[i]
    candidates.append(multi) 

# 모두 음수일 경우
if len(positive) == 0:
    multi = 1
    for i in range(-1, -4, -1):
        multi *= negative[i]
    candidates.append(multi)
if len(positive) >= 3:
    multi = 1
    # 모두 양수일 경우 
    for i in range(-1, -4, -1):
        multi *= positive[i]
    candidates.append(multi)
if len(negative) >= 2 and len(positive) >= 1:
    multi = 1
    # 2개의 음수, 1개의 양수:
    multi = negative[0]*negative[1]*positive[-1]
    candidates.append(multi)

print(max(candidates))

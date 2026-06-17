pos = list(map(int, input().split()))
pos = sorted(pos)
left, mid, right = pos

# 연속된 숫자
if right - left == 2:
    print(0)
elif mid - left == 2 or right - mid == 2: # 들어갈 자리가 하나인 경우 [6, 8, 9]
    print(1)
else:
    print(2)
n = int(input())

a = 0 # 교실 이틀
b = 0 # 복도 3일
c = 0 # 12일

days = [0]*(n+1)

for i in range(2, n+1, 2):
    days[i] = 2

for i in range(3, n+1, 3):
    if days[i] <= 3:
        days[i] = 3

for i in range(12, n+1, 12):
    if days[i] <= 12:
        days[i] = 12

for i in range(n+1):
    if days[i] == 2:
        a += 1
    elif days[i] == 3:
        b += 1
    elif days[i] == 12:
        c += 1

print(a, b, c)

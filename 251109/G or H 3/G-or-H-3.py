n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

r = max(x)
arr=['']*(r+1)
for i in range(n):
    arr[x[i]] = c[i]  # pos 위치에 char 저장

if k >= r:
    start_range = 1
    end_range = r
else:
    start_range = 1
    end_range = r - k + 1
    
max_value = 0
for i in range(start_range, end_range + 1):
    total = 0
    # [i, i+k] 범위 검사 (끝 포함)
    for j in range(i, min(i + k + 1, len(arr))):
        if arr[j] == 'G':
            total += 1
        elif arr[j] == 'H':
            total += 2
    max_value = max(max_value, total)
print(max_value)   


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_count = 0
for i in range(n):
    for j in range(n-2):
        count1 = 0
        # 첫 번째 행
        for k in range(j, j+3):
            if arr[i][k] == 1:
                count1 += 1
        # 두 번째 행
        for a in range(i, n):
            for b in range(n-2):
                if a == i and not (b > j + 2 or j > b + 2):
                    continue
                count2 = 0
                for k in range(b, b+3):
                    if arr[a][k] == 1:
                        count2 += 1
                total = count1 + count2
                max_count = max(max_count, total)
            
print(max_count)

        

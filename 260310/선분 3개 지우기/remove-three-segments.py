n = int(input())
segments = []
for _ in range(n):
    left, right = map(int, input().split())
    segments.append((left, right))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            remaining = []
            for m in range(n):
                if m!=i and m!=j and m!=k:
                    remaining.append(segments[m])
            
            remaining.sort()
            
            is_overlap = False
            for idx in range(len(remaining)-1):
                if remaining[idx][1] >= remaining[idx+1][0]:
                    is_overlap = True
                    break
            if not is_overlap:
                ans += 1
            
print(ans)      


N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

total = 0
max_count = 0

for i in range(N):
    b = P[i] // 2
    total = b
    #print(f'total:{total}, i:{i}, b:{b}')
    count = 1
    for j in range(N):
        if i == j:
            continue
        total += P[j]
        count += 1
        #print(f'total:{total}, P[j]:{P[j]}, count:{count}, j:{j}')
        if total <= B:
            max_count = max(max_count, count)

print(max_count)
        


    




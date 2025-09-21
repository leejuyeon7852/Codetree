N, M = map(int, input().split())
MAX = 1000 * 1000
pos_a, pos_b = [0] * (MAX + 1), [0] * (MAX + 1)

# Process A's movements
time_a = 1
cur_a = 0
for _ in range(N):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        cur_a += vi
        pos_a[time_a] = cur_a
        time_a += 1

# Process B's movements
time_b = 1
cur_b = 0
for _ in range(M):
    vi, ti = map(int, input().split())
    for _ in range(ti):
        cur_b += vi
        pos_b[time_b] = cur_b
        time_b += 1

# # 확인용 출력
# for i in range(time_a):
#     print(pos_a[i], end=" ")
# print()
# for i in range(time_b):
#     print(pos_b[i], end=" ")

# 선두 찾기
lead = ''
count = 0
for i in range(time_a):
    if pos_a[i] > pos_b[i]:
        if lead == 'B' or lead == 'All':
            count += 1
        lead = 'A'
    elif pos_a[i] < pos_b[i]: #B가 lead 일때
        if lead == 'A' or lead == 'All':
            count+= 1
        lead = 'B'
    elif pos_a[i] == pos_b[i]:
        if lead == 'B' or lead == 'A':
            count += 1
        lead = 'All'
print(count)

        
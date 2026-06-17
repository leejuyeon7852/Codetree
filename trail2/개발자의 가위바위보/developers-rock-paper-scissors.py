N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]

max_count = 0

wins = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}

candidates = [
    {1: '가위', 2:'바위', 3:'보'},
    {1:'가위', 2:'보', 3:'바위'},
    {1:'바위',2:'가위', 3:'보'},
    {1:'바위', 2:'보', 3:'가위'},
    {1:'보', 2:'가위', 3:'바위'},
    {1:'보', 2:'바위', 3:'가위'}
]

for candidate in candidates:
    count = 0
    for a, b in moves:
        if wins[candidate[a]] == candidate[b]:
            count += 1
    max_count = max(max_count, count)

print(max_count)



# # 변수 선언 및 입력
# n = int(input())
# arr = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]

# max_win = 0

# # Case 1. 1이 2를 이기고, 2가 3을 이기고 3이 1을 이기는 경우
# win = 0
# for a, b in arr:
#     if a == 1 and b == 2:
#         win += 1
#     elif a == 2 and b == 3:
#         win += 1
#     elif a == 3 and b == 1:
#         win += 1

# max_win = max(max_win, win)

# # Case 2. 1이 3을 이기고, 3이 2를 이기고 2가 1을 이기는 경우
# win = 0
# for a, b in arr:
#     if a == 1 and b == 3:
#         win += 1
#     elif a == 3 and b == 2:
#         win += 1
#     elif a == 2 and b == 1:
#         win += 1

# max_win = max(max_win, win)

# print(max_win)

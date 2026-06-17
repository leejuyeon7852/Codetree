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
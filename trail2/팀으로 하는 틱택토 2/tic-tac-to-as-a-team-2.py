inp = [input() for _ in range(3)]
board = [[int(c) for c in row] for row in inp]

nums = set()
for row in board:
    for n in row:
        nums.add(n)

lines = []
for i in range(3):
    lines.append(board[i])  # 가로
    lines.append([board[r][i] for r in range(3)])  # 세로

# 대각선 2개
lines.append([board[i][i] for i in range(3)])
lines.append([board[i][2-i] for i in range(3)])

# print(lines)

count = 0
for i in nums:
    for j in nums:
        if i >= j:
            continue
        for line in lines:
            if all(x == i or x == j for x in line) and (i in line and j in line):
                count += 1
                break # 팀의 개수만 세면 됨
print(count)
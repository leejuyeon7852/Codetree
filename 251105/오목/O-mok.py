import sys
board = [list(map(int, input().split())) for _ in range(19)]

n = 19

for i in range(n):
    for j in range(n):
        # 검은색
        if board[i][j] == 1:
            # 가로 방향
            if j+4 < n:
                for k in range(5):
                    if board[i][j+k] != 1:
                        break
                else:
                    print(1)
                    print(i+1, j+3) # 가운데 좌표
                    sys.exit()
            # 세로 방향
            if i+4 < n:
                for k in range(5):
                    if board[i+k][j] != 1:
                        break
                else:
                    print(1)
                    print(i+3, j+1)
                    sys.exit()
            # 대각선 방향 (오른쪽 밑)
            if i + 4 < n and j + 4 < n:
                for k in range(5):
                    if board[i+k][j+k] != 1:
                        break
                else:
                    print(1)
                    print(i+3, j+3)
                    sys.exit()
            # 대각선 방향 (오른쪽 위)
            if i-4 >= 0 and j+4 < n:
                for k in range(5):
                    if board[i - k][j + k] != 1:
                            break
                else:
                    print(1)
                    print(i - 2, j + 3)
                    sys.exit()
        # 흰색
        if board[i][j] == 2:
            # 가로 방향
            if j+4 < n:
                for k in range(5):
                    if board[i][j+k] != 2:
                        break
                else:
                    print(2)
                    print(i+1, j+3) # 가운데 좌표
                    sys.exit()
            # 세로 방향
            if i+4 < n:
                for k in range(5):
                    if board[i+k][j] != 2:
                        break
                else:
                    print(2)
                    print(i+3, j+1)
                    sys.exit()
            # 대각선 방향 (오른쪽 밑)
            if i + 4 < n and j + 4 < n:
                for k in range(5):
                    if board[i+k][j+k] != 2:
                        break
                else:
                    print(2)
                    print(i+3, j+3)
                    sys.exit()
            # 대각선 방향 (오른쪽 위)
            if i-4 >= 0 and j+4 < n:
                for k in range(5):
                    if board[i - k][j + k] != 2:
                        break
                else:
                    print(2)
                    print(i - 2, j + 3)
                    sys.exit()
print(0)
n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

if max(x1) <= min(x2):
    print('Yes')
else:
    print('No')

m, f = map(int, input().split())

money = 0
if m >= 90 and f >= 90:
    if f >= 95:
        money = 100000
    else:
        money = 50000

print(money)
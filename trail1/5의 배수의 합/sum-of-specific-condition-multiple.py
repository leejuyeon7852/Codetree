a, b = map(int, input().split())


if a > b:
    sum = 0
    for i in range(b, a+1):
        if i % 5 == 0:
            sum += i
else:
    sum = 0
    for i in range(a, b+1):
        if i % 5 == 0:
            sum += i
print(sum)
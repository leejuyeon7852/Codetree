A, B = map(int, input().split())

i = A
while A <= i <= B:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1
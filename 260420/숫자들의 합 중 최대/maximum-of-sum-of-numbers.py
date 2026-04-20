X, Y = map(int, input().split())

max = 0

for i in range(X, Y+1):
    digit_sum = sum(map(int, str(i)))
    if digit_sum > max :
        max = digit_sum

print(max)
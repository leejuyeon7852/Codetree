a, b = map(int, input().split())
sum = 0
count = 0
for i in range(a, b+1):
    if (i%5==0) or (i%7==0):
        sum += i
        count += 1

avg = sum/count

print(sum, f'{avg:.1f}')




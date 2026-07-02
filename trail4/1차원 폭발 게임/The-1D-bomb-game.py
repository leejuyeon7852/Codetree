n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

while True:
    temp = []
    idx = 0
    exploded = False

    while idx < n:
        next_idx = idx

        while next_idx < n and numbers[next_idx] == numbers[idx]:
            next_idx += 1
        
        if next_idx - idx < m:
            for i in range(idx, next_idx):
                temp.append(numbers[i])
        else:
            exploded = True
            
        idx = next_idx
    
    numbers = temp
    n = len(numbers)

    if not exploded:
        break

print(n)
for num in numbers:
    print(num)



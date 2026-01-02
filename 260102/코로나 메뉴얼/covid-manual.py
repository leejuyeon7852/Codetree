countA = 0 
for _ in range(3):
    is_cold, temp = input().split()
    temp = int(temp)
    if is_cold == 'Y' and temp >= 37:
        countA += 1
    
if countA >= 2:
    print('E')
else:
    print('N')
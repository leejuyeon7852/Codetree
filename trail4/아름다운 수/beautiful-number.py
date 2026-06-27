n = int(input())
arr = []
count = 0

def beautiful_num(cnt):
    global count

    if cnt == n:
        #print(arr)
        count += 1
        return 
    
    for i in range(1, 5):
        if cnt + i > n:
            continue
        
        # for _ in range(i): # i만큼 값 넣어주기
        #     arr.append(i)

        beautiful_num(cnt+i)

        # for _ in range(i): # 원상 복구
        #     arr.pop()
    

beautiful_num(0)
print(count)

X, Y = map(int, input().split())

count = 0

for n in range(X, Y+1):
    flag = True
    n = list(map(int, str(n))) # 굳이 정수로 또 바꾸 필요 없음
    for i in range(len(n)//2):
        if n[i] != n[len(n)-1-i]:
            flag = False
            break    
    if flag:
        count += 1

print(count)

# count = 0
# for i in range(X, Y+1):
#     str_i = str(i)

#     if str_i == str_i[::-1]:
#         ans += 1
# print(ans)
                   